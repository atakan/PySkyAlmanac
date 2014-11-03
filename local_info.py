#!/usr/bin/python
# -*- coding: utf-8 -*-

#    Copyright (C) 2011  Mehmet Atakan Gürkan
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License version 3 as
#    published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program (probably in a file named COPYING).
#    If not, see <http://www.gnu.org/licenses/>.

from __future__ import division, print_function

import datetime, calendar, ephem, pytz, pyx, time
from datetime import timedelta as TD

from almanac_utils import *
from translations import t

# Local stuff: Here we set the observer's location, timezone and DST
# conventions.
# In addition we set the year for the chart, the limits for the chart,
# and make arrangements for the twilight lines.

use_city = True
use_today = True
use_your_timezone = True

if(use_city):
    obs_city = 'San Francisco' #See which cities are valid at https://github.com/brandon-rhodes/pyephem/blob/master/ephem/cities.py
    obs = ephem.city(obs_city)
else:
    #Deland, Florida
    obs = ephem.Observer()
    obs.lat  = '29.0225'
    obs.long = '-81.286389'
    obs.elevation = 11.0
    #obs.temp = 15.0
    #obs.pressure = 1010.0

if(use_today):
    obs_date = datetime.date.today()
else:
    obs_date = datetime.date(2015,3,4)

if(use_your_timezone):
    if(time.localtime().tm_isdst):
        offsetHour = time.altzone / 3600
    else:
        offsetHour = time.timezone / 3600
    # TODO: the chart needs to account for negatives, returns 7 instead of -7 during PST daylight savings time. At the moment using the wrong timezone!
    my_tz = 'Etc/GMT{0:+d}'.format(int(offsetHour))
    obsTZ = pytz.timezone(str(my_tz))
else:
    #obsTZ = pytz.timezone('US/Pacific')
    #obsTZ = pytz.timezone('Europe/Istanbul')
    #obsTZ = pytz.timezone('EET') # Turkey uses Eastern European Time: UTC+2 normal time, +3 summer time
    #obsTZ = pytz.timezone('Etc/GMT+2')
    #obsTZ = pytz.timezone('Etc/GMT+8') # UTC+8 for Chinese Standard time
    obsTZ = pytz.timezone('Etc/GMT-8') # UTC-8 for PST, UTC-7 during daylight savings time.

utcTZ = pytz.timezone('UTC')
year = obs_date.year
begin_day_datetime = datetime.datetime(year-1, 12, 31, 12, tzinfo=obsTZ) # noon of the last day of previous year
begin_day = ephem.Date(begin_day_datetime.astimezone(utcTZ)) # convert to UTC
hrs_utc_offset = -(24.*obsTZ.utcoffset(begin_day,is_dst=time.localtime().tm_isdst).days + obsTZ.utcoffset(begin_day,is_dst=time.localtime().tm_isdst).seconds/3600)
if calendar.isleap(year) :
    no_days = 367
else :
    no_days = 366

for first_sunday in range(1,8) :
    if calendar.weekday(year, 1, first_sunday) == calendar.SUNDAY :
        break
first_sunday_datetime = datetime.datetime(year, 1, first_sunday, 12, tzinfo=obsTZ)

# Can calculate sunrise/set and twilight http://rhodesmill.org/pyephem/rise-set.html
# According to Naval Astronomical Almanac, set horizon to 34 arcminutes lower than normal horizon, and pressure to zero.
# In addition to this, we want the latest sunrise, and the earliest sunset. We
# can't directly use the solstice though, but the order is always the same;
# earliest sunset, winter solstice, then latest sunrise.
# References:
# http://earthsky.org/tonight/latest-sunrises-for-midnorthern-latitudes-in-early-january
# http://aa.usno.navy.mil/faq/docs/rs_solstices.php
temp_pressure = obs.pressure # Stash observer pressure and horizon
temp_horizon = obs.horizon # Just in case set other than zero for an experimental observer
obs.pressure = 0
obs.horizon = '-0:34' # 34 arcminutes lower than normal horizon
# We know that the date of the solstice doesn't give us the dates we want, but
# for now, I will round up/down for that date until can calculate more accurately.
# Will be okay for people next to the equator and less accurate the closer you get to the arctic/antarctic circles.
solstice_date = ephem.date(ephem.next_solstice(obs_date) - hrs_utc_offset*ephem.hour)
if(solstice_date.triple()[0]>obs_date.year): # make a check for running this code after the solstice
    solstice_date = ephem.date(ephem.previous_solstice(obs_date) - hrs_utc_offset*ephem.hour)
# Calculate Earliest Sunset
obs_sunset = ephem.date(obs.previous_setting(ephem.Sun(), solstice_date) - hrs_utc_offset*ephem.hour)
# Calculate Latest Sunrise
obs_sunrise = ephem.date(obs.next_rising(ephem.Sun(), solstice_date) - hrs_utc_offset*ephem.hour)
print('earliest sunset: {}'.format(obs_sunset))
print('solstice: {}'.format(solstice_date))
print('latest sunrise: {}'.format(obs_sunrise))
# Put values back
obs.pressure = temp_pressure
obs.horizon = temp_horizon
earliest_sunset = obs_sunset.tuple()[3] - 12 #(PM)
latest_sunrise = obs_sunrise.tuple()[3] + 1 #(AM), add one to round to end of hour
print('{}PM to {}AM will be the bounds of the chart'.format(earliest_sunset,latest_sunrise))

## In Turkey (and in most of Europe), DST rules are:
## Start: Last Sunday in March
## End: Last Sunday in October
## Time: 1.00 am (01:00) Greenwich Mean Time (GMT)
## http://wwp.greenwichmeantime.com/time-zone/rules/eu/index.htm
#for week in range(53) :
#    sunday_datetime = first_sunday_datetime + TD(days=7*week)
#    if (sunday_datetime.month == 3 and
#        (sunday_datetime+TD(days=7)).month == 4) :
#        dst_begin = ephem.Date(sunday_datetime.astimezone(utcTZ))
#    if (sunday_datetime.month == 10 and
#        (sunday_datetime+TD(days=7)).month == 11) :
#        dst_end = ephem.Date(sunday_datetime.astimezone(utcTZ))

import bodies
