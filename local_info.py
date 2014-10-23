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
    obs = ephem.Observer()
    obs.lat  = '30.669444'
    obs.long = '-81.461667'
    obs.elevation = 7.6
    #obs.temp = 15.0
    #obs.pressure = 1010.0

if(use_today):
    obs_date = datetime.date.today()
else:
    obs_date = datetime.date(2015,3,4)

if(use_your_timezone):
    if time.daylight:
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
    obsTZ = pytz.timezone('Etc/GMT-7') # UTC-8 for PST, UTC-7 during daylight savings time.

utcTZ = pytz.timezone('UTC')
year = obs_date.year
begin_day_datetime = datetime.datetime(year-1, 12, 31, 12, tzinfo=obsTZ) # noon of the last day of previous year
begin_day = ephem.Date(begin_day_datetime.astimezone(utcTZ)) # convert to UTC
hrs_utc_offset = -(24.*obsTZ.utcoffset(begin_day,is_dst=time.daylight).days + obsTZ.utcoffset(begin_day,is_dst=time.daylight).seconds/3600)
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

# Objects to be plotted on the chart
# planets
mercury = PyEph_body(ephem.Mercury(), color.cmyk.BurntOrange)
venus =   PyEph_body(ephem.Venus(), color.cmyk.CornflowerBlue)
mars =    PyEph_body(ephem.Mars(), color.cmyk.Red)
jupiter = PyEph_body(ephem.Jupiter(), color.cmyk.Magenta)
saturn =  PyEph_body(ephem.Saturn(), color.cmyk.Yellow)
uranus =  PyEph_body(ephem.Uranus(), color.cmyk.SpringGreen)
neptune = PyEph_body(ephem.Neptune(), color.cmyk.ForestGreen)
# some messier objects
m1 = PyEph_body(ephem.readdb("M1,f|R,05:34:30,22:01,8.4,2000,360"), symbol='m1', tsize='tiny')
m13 = PyEph_body(ephem.readdb("M13,f|C,16:41:42,36:28,5.9,2000,996"), symbol='m13', tsize='tiny')
m31 = PyEph_body(ephem.readdb("M31,f|G,0:42:44,+41:16:8,4.16,2000,11433|3700|35"), symbol='m31', tsize='tiny')
m42 = PyEph_body(ephem.readdb("M42,f|U,05:35:18,-05:23,4,2000,3960"), symbol='m42', tsize='tiny')
m45 = PyEph_body(ephem.readdb("M45,f|U,03:47:0,24:07,1.2,2000,6000"), symbol='m45', tsize='tiny')
m57 = PyEph_body(ephem.readdb("M57,f|P,18:53:36,33:02,9,2000,86"), symbol='m57', tsize='tiny')
m97 = PyEph_body(ephem.readdb("M97,f|P,11:14:48,55:01,11,2000,202"), symbol='m97', tsize='tiny')
# some bright stars
sirius     = PyEph_body(ephem.star('Sirius'), symbol='Sir', tsize='tiny')
antares    = PyEph_body(ephem.star('Regulus'), symbol='Ant', tsize='tiny')
deneb      = PyEph_body(ephem.star('Deneb'), symbol='Den', tsize='tiny')
betelgeuse = PyEph_body(ephem.star('Betelgeuse'), symbol='Bet', tsize='tiny')
pollux     = PyEph_body(ephem.star('Pollux'), symbol='Pol', tsize='tiny')
arcturus   = PyEph_body(ephem.star('Arcturus'), symbol='Arc', tsize='tiny')

mercury.rising_text = [
[0.1, t['mercury'], t['rises'], -1, True],
[0.43, t['mercury'], t['rises'], -1, False],
[0.72, t['mercury'], t['rises'], -1, True],
[0.931, t['mercury'], t['rises'], -1, False]
]
venus.rising_text = [
[0.1, t['venus']+' '+t['rises'], '~', -1, True]
]
mars.rising_text = [
[0.55, t['mars']+' '+t['rises'], '~', 0, False]
]
jupiter.rising_text = [
[0.6, t['jupiter']+' '+t['rises'], '~', 0, False]
]
saturn.rising_text = [
[0.14, t['saturn']+' '+t['rises'], '~', 0, False],
[0.83, t['saturn']+' '+t['rises'], '~', 0, False]
]
uranus.rising_text = [
[0.6, t['uranus']+' '+t['rises'], '~', -1, False]
]
neptune.rising_text = [
[0.34, t['neptune']+' '+t['rises'], '~', 0, False]
]
m31.rising_text = [
[0.24, 'M31 '+t['rises'], '~', 0, False]
]
m45.rising_text = [
[0.57, 'M45 '+t['rises'], '~', 0, False]
]
m42.rising_text = [
[0.73, 'M42 '+t['rises'], '~', 0, False]
]
antares.rising_text = [
[0.1, t['antares']+' '+t['rises'], '~', 0, False],
[0.87, t['antares']+' '+t['rises'], '~', 0, False]
]
mars.transit_text = [
[0.925, t['mars']+' '+t['transits'], '~', 0, False]
]
jupiter.transit_text = [
[0.7, t['jupiter']+' '+t['transits'], '~', 0, False]
]
saturn.transit_text = [
[0.25, t['saturn']+' '+t['transits'], '~', 0, False]
]
uranus.transit_text = [
[0.75, '~', t['uranus']+' '+t['transits'], -1, False]
]
neptune.transit_text = [
[0.67, t['neptune']+' '+t['transits'], '~', 0, False]
]
m31.transit_text = [
[0.035, '~', 'M31 '+t['transits'], -1, False],
[0.77, '~', 'M31 '+t['transits'], -1, False]
]
m45.transit_text = [
[0.08, '~', 'M45 '+t['transits'], -1, False],
[0.83, '~', 'M45 '+t['transits'], -1, False]
]
m42.transit_text = [
[0.13, 'M42 '+t['transits'], '~', 0, False],
[0.87, 'M42 '+t['transits'], '~', 0, False]
]
m57.transit_text = [
[0.13, 'M57 '+t['transits'], '~', 0, False],
[0.87, 'M57 '+t['transits'], '~', 0, False]
]
antares.transit_text = [
[0.18, t['antares']+' '+t['transits'], '~', 0, False],
[0.963, t['antares']+' '+t['transits_abbrev'], '~', 0, False]
]
arcturus.transit_text = [
[0.2, t['arcturus']+' '+t['transits'], '~', 0, False]
]
pollux.transit_text = [
[0.2, t['pollux'], t['transits'], -1, False],
[0.94, t['pollux']+' '+t['transits'], '~', 0, False]
]
deneb.transit_text = [
[0.68, t['deneb']+' '+t['transits'], '~', 0, False],
]
mercury.setting_text = [
[0.25, t['mercury'], t['sets'], -1, False],
[0.51, t['mercury'], t['sets'], -1, False],
[0.89, t['mercury'], t['sets'], -1, False]
]
venus.setting_text = [
[0.91, t['venus']+' '+t['sets'], '~', 0, True],
]
mars.setting_text = [
[0.07, '~', t['mars']+' '+t['sets_abbrev'], -1, False]
]
jupiter.setting_text = [
[0.1, '~', t['jupiter']+' '+t['sets'], -1, False],
[0.9, '~', t['jupiter']+' '+t['sets'], -1, False]
]
saturn.setting_text = [
[0.4, t['saturn']+' '+t['sets'], '~', 0, False]
]
uranus.setting_text = [
[0.13, '~', t['uranus']+' '+t['sets'], -1, False],
[0.87, '~', t['uranus']+' '+t['sets'], -1, False]
]
neptune.setting_text = [
[0.09, t['neptune']+' '+t['sets'], '~', 0, False],
[0.78, t['neptune']+' '+t['sets'], '~', 0, False]
]
m31.setting_text = [
[0.15, '~', 'M31 '+t['sets'], -1, False],
[0.94, '~', 'M31 '+t['sets'], -1, False]
]
m45.setting_text = [
[0.35, '~', 'M45 '+t['sets'], -1, False],
[0.960, '~', 'M45 '+t['sets'], -1, False]
]
m42.setting_text = [
[0.35, 'M42 '+t['sets'], '~', 0, False],
[0.965, 'M42 '+t['sets'], '~', 0, False]
]
antares.setting_text = [
[0.45, t['antares']+' '+t['sets'], '~', 0, False]
]

rising_bodies  = [mercury, venus, mars, jupiter, uranus, neptune,
                  m31, m42, m45, m57,
                  sirius, antares, deneb, betelgeuse, pollux]
setting_bodies = [mercury, venus, mars, jupiter, uranus, neptune,
                  m31, m42, m45, m57,
                  sirius, antares, deneb, betelgeuse, pollux]
transit_bodies = [mars, jupiter, uranus, neptune,
                  m31, m42, m45, m57,
                  sirius, antares, deneb, betelgeuse, pollux]

rising_bodies  = [mars]
setting_bodies = [mars]
transit_bodies = [mars]

rising_bodies  = [
                  m31, m42, m45, m57,
                  mercury, venus, mars, jupiter, saturn, uranus, neptune]
setting_bodies = [
                  m31, m42, m45, m57,
                  mercury, venus, mars, jupiter, saturn, uranus, neptune]
transit_bodies = [antares, deneb, arcturus, pollux,
                  m31, m42, m45, m57,
                  mars, jupiter, saturn, uranus, neptune]
