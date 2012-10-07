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

import datetime, calendar, ephem, pytz, pyx
from datetime import timedelta as TD

from almanac_utils import *

# Local stuff: Here we set the observer's location, timezone and DST
# conventions.
# In addition we set the year for the chart, the limits for the chart,
# and make arrangements for the twilight lines.

obs = ephem.Observer()
# bodrum
#obs.lat  = '37.04'
#obs.long = '27.43'
# ankara
obs.lat  = '39.877'
obs.long = '32.807'
#obsTZ = pytz.timezone('Europe/Istanbul')
obsTZ = pytz.timezone('EET') # Turkey uses Eastern European Time: UTC+2 normal time, +3 summer time
utcTZ = pytz.timezone('UTC')

year = 2011
begin_day_datetime = datetime.datetime(year-1, 12, 31, 12, tzinfo=obsTZ) # noon of the last day of previous year
begin_day = ephem.Date(begin_day_datetime.astimezone(utcTZ)) # convert to UTC
if calendar.isleap(year) :
    no_days = 367
else :
    no_days = 366

for first_sunday in range(1,8) :
    if calendar.weekday(year, 1, first_sunday) == calendar.SUNDAY :
        break
first_sunday_datetime = datetime.datetime(year, 1, first_sunday, 12, tzinfo=obsTZ)

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
m13 = PyEph_body(ephem.readdb("M13,f|C,16:41:42,36:28,5.9,2000,996"),
        symbol='m13', tsize='tiny')
m31 = PyEph_body(ephem.readdb("M31,f|G,0:42:44,+41:16:8,4.16,2000,11433|3700|35"),
        symbol='m31', tsize='tiny')
m42 = PyEph_body(ephem.readdb("M42,f|U,05:35:18,-05:23,4,2000,3960"),
        symbol='m42', tsize='tiny')
m45 = PyEph_body(ephem.readdb("M45,f|U,03:47:0,24:07,1.2,2000,6000"),
        symbol='m45', tsize='tiny')
# some bright stars
sirius     = PyEph_body(ephem.star('Sirius'), symbol='Sir', tsize='tiny')
antares    = PyEph_body(ephem.star('Regulus'), symbol='Ant', tsize='tiny')
deneb      = PyEph_body(ephem.star('Deneb'), symbol='Den', tsize='tiny')
betelgeuse = PyEph_body(ephem.star('Betelgeuse'), symbol='Bet', tsize='tiny')
pollux     = PyEph_body(ephem.star('Pollux'), symbol='Pol', tsize='tiny')
arcturus   = PyEph_body(ephem.star('Arcturus'), symbol='Arc', tsize='tiny')

mercury.rising_text = [
[0.1, 'Merkür', 'doğuyor', -1, True],
[0.43, 'Merkür', 'doğuyor', -1, False],
[0.72, 'Merkür', 'doğuyor', -1, True],
[0.931, 'Merkür', 'doğuyor', -1, False]
]
venus.rising_text = [
[0.1, 'Venüs doğuyor', '~', -1, True]
]
mars.rising_text = [
[0.55, 'Mars doğuyor', '~', 0, False]
]
jupiter.rising_text = [
[0.6, 'Jüpiter doğuyor', '~', 0, False]
]
saturn.rising_text = [
[0.14, 'Satürn doğuyor', '~', 0, False],
[0.83, 'Satürn doğuyor', '~', 0, False]
]
uranus.rising_text = [
[0.6, 'Uranüs doğuyor', '~', -1, False]
]
neptune.rising_text = [
[0.34, 'Neptün doğuyor', '~', 0, False]
]
m31.rising_text = [
[0.24, 'M31 doğuyor', '~', 0, False]
]
m45.rising_text = [
[0.57, 'M45 doğuyor', '~', 0, False]
]
m42.rising_text = [
[0.73, 'M42 doğuyor', '~', 0, False]
]
antares.rising_text = [
[0.1, 'Antares doğuyor', '~', 0, False],
[0.87, 'Antares doğuyor', '~', 0, False]
]

mars.transit_text = [
[0.925, 'Mars meridyende', '~', 0, False]
]
jupiter.transit_text = [
[0.7, 'Jüpiter meridyende', '~', 0, False]
]
saturn.transit_text = [
[0.25, 'Satürn meridyende', '~', 0, False]
]
uranus.transit_text = [
[0.75, '~', 'Uranüs meridyende', -1, False]
]
neptune.transit_text = [
[0.67, 'Neptün meridyende', '~', 0, False]
]
m31.transit_text = [
[0.035, '~', 'M31 meridyende', -1, False],
[0.77, '~', 'M31 meridyende', -1, False]
]
m45.transit_text = [
[0.08, '~', 'M45 meridyende', -1, False],
[0.83, '~', 'M45 meridyende', -1, False]
]
m42.transit_text = [
[0.13, 'M42 meridyende', '~', 0, False],
[0.87, 'M42 meridyende', '~', 0, False]
]
antares.transit_text = [
[0.18, 'Antares meridyende', '~', 0, False],
[0.963, 'Antares mrd.', '~', 0, False]
]
arcturus.transit_text = [
[0.2, 'Arcturus meridyende', '~', 0, False]
]
pollux.transit_text = [
[0.2, 'Pollux', 'meridyende', -1, False],
[0.94, 'Pollux meridyende', '~', 0, False]
]
deneb.transit_text = [
[0.68, 'Deneb meridyende', '~', 0, False],
]

mercury.setting_text = [
[0.25, 'Merkür', 'batıyor', -1, False],
[0.51, 'Merkür', 'batıyor', -1, False],
[0.89, 'Merkür', '~~batıyor', -1, False]
]
venus.setting_text = [
[0.91, 'Venüs batıyor', '~', 0, True],
]
mars.setting_text = [
[0.07, '~', 'Mars bt.', -1, False]
]
jupiter.setting_text = [
[0.1, '~', 'Jüpiter batıyor', -1, False],
[0.9, '~', 'Jüpiter batıyor', -1, False]
]
saturn.setting_text = [
[0.4, 'Satürn batıyor', '~', 0, False]
]
uranus.setting_text = [
[0.13, '~', 'Uranüs batıyor', -1, False],
[0.87, '~', 'Uranüs batıyor', -1, False]
]
neptune.setting_text = [
[0.09, 'Neptün batıyor', '~', 0, False],
[0.78, 'Neptün batıyor', '~', 0, False]
]
m31.setting_text = [
[0.15, '~', 'M31 batıyor', -1, False],
[0.94, '~', 'M31 batıyor', -1, False]
]
m45.setting_text = [
[0.35, '~', 'M45 batıyor', -1, False],
[0.960, '~', 'M45 batıyor', -1, False]
]
m42.setting_text = [
[0.35, 'M42 batıyor', '~', 0, False],
[0.965, 'M42 batıyor', '~', 0, False]
]
antares.setting_text = [
[0.45, 'Antares batıyor', '~', 0, False]
]

rising_bodies  = [mercury, venus, mars, jupiter, uranus, neptune,
                  m31, m42, m45,
                  sirius, antares, deneb, betelgeuse, pollux]
setting_bodies = [mercury, venus, mars, jupiter, uranus, neptune,
                  m31, m42, m45,
                  sirius, antares, deneb, betelgeuse, pollux]
transit_bodies = [mars, jupiter, uranus, neptune,
                  m31, m42, m45,
                  sirius, antares, deneb, betelgeuse, pollux]

rising_bodies  = [mars]
setting_bodies = [mars]
transit_bodies = [mars]

rising_bodies  = [ 
                  m31, m42, m45,
                  mercury, venus, mars, jupiter, saturn, uranus, neptune]
setting_bodies = [
                  m31, m42, m45,
                  mercury, venus, mars, jupiter, saturn, uranus, neptune]
transit_bodies = [antares, deneb, arcturus, pollux,
                  m31, m42, m45,
                  mars, jupiter, saturn, uranus, neptune]

