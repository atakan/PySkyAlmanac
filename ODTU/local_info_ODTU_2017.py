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
#obs.lat  = '39.877'
#obs.long = '32.807'
#odtu fizik
obs.lat  = '39.895'
obs.long = '32.782'
# Sabancı Üniversitesi
#obs.lat = '40.8918'
#obs.long = '29.3787'
#obsTZ = pytz.timezone('Europe/Istanbul')
obsTZ = pytz.timezone('Europe/Istanbul') # Turkey now uses UTC+3 continuously
utcTZ = pytz.timezone('UTC')

year = 2017
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
[0.1, 'Merkür', 'doğuyor', -1, False],
[0.44, 'Merkür', 'doğuyor', -1, False],
[0.74, 'Merkür', 'doğuyor', -1, True],
[0.965, 'Merkür', 'doğ.', -1, False]
]
venus.rising_text = [
[0.55, 'Venüs doğuyor', '~', 0, False]
]
mars.rising_text = [
[0.83, 'Mars doğuyor',  '~',-2, False]
]
jupiter.rising_text = [
[0.1, '~', 'Jüpiter doğuyor', -1, False],
[0.9, 'Jüpiter doğuyor', '~', 0, False]
]
saturn.rising_text = [
[0.15, 'Satürn doğuyor', '~', 0, False],
[0.98, 'Sat. doğ.', '~', -1, False]
]
uranus.rising_text = [
[0.5, '~', 'Uranüs doğuyor', -1, False]
]
neptune.rising_text = [
[0.46, 'Neptün doğuyor', '~', -1, False]
]
m31.rising_text = [
[0.24, '~', 'M31 doğuyor', 0, False]
]
m45.rising_text = [
[0.67, 'M45 doğuyor', '~', 0, False]
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
[0.33, 'Jüpiter meridyende', '~', 0, False],
[0.98, 'Jüp. mrd.', '~', 0, False]
]
saturn.transit_text = [
[0.4, '~', 'Satürn meridyende', 0, False]
]
uranus.transit_text = [
[0.06, 'Uranüs', 'meridyende', -1, False],
[0.79,'Uranüs meridyende', '~',  -1, False]
]
neptune.transit_text = [
[0.7, 'Neptün meridyende', '~', 0, False]
]
m31.transit_text = [
[0.042, 'M31 mrd.', '~', 0, False],
[0.7, 'M31 meridyende', '~', 0, False]
]
m45.transit_text = [
[0.10, 'M45 meridyende', '~', 0, False],
[0.85, 'M45 meridyende', '~', 0, False]
]
m42.transit_text = [
[0.09, '~', 'M42 meridyende', 0, False],
[0.87, 'M42 meridyende', '~', 0, False]
]
antares.transit_text = [
[0.18, 'Antares meridyende', '~', 0, False],
[0.963, 'Antares mrd.', '~', 0, False]
]
arcturus.transit_text = [
[0.24, 'Arcturus meridyende', '~', 0, False]
]
pollux.transit_text = [
[0.12, 'Pollux meridyende', '~', -1, False],
[0.88, 'Pollux meridyende', '~', -1, False]
]
deneb.transit_text = [
[0.68, '~', 'Deneb meridyende', 0, False],
]

mercury.setting_text = [
[0.04, 'Mrk', 'bat.', -1, False],
[0.22, 'Merkür', 'batıyor', -1, True],
[0.59, 'Merkür', '~', -1, False],
[0.56, 'batıyor', '~', -1, False],
[0.89, 'Merkür', 'batıyor', -1, True]
]
venus.setting_text = [
[0.2, 'Venüs batıyor', '~', 0, False]
]
mars.setting_text = [
[0.3, 'Mars batıyor', '~', 0, False],
[0.9, 'Mars batıyor', '~', 0, False]
]
jupiter.setting_text = [
[0.45,'Jüpiter batıyor', '~',  -1, False],
]
saturn.setting_text = [
[0.75,'Satürn batıyor', '~',  -1, False]
]
uranus.setting_text = [
[0.21, '~', 'Uranüs batıyor', -1, False],
[0.88, '~', 'Uranüs batıyor', -1, False]
]
neptune.setting_text = [
[0.1, 'Neptün batıyor', '~', -1, False],
[0.87, 'Neptün batıyor', '~', -1, False]
]
m31.setting_text = [
[0.20, '~', 'M31 batıyor', -1, False],
[0.93, '~', 'M31 batıyor', -1, False]
]
m45.setting_text = [
[0.19, '~', 'M45 batıyor', -1, False],
[0.930, '~', 'M45 batıyor', -1, False]
]
m42.setting_text = [
[0.15, 'M42 batıyor', '~', 0, False],
[0.97, 'M42 batıyor', '~', 0, False]
]
antares.setting_text = [
[0.45, 'Antares batıyor', '~', 0, False]
]

#rising_bodies  = [mercury, venus, mars, jupiter, uranus, neptune,
#                  m31, m42, m45,
#                  sirius, antares, deneb, betelgeuse, pollux]
#setting_bodies = [mercury, venus, mars, jupiter, uranus, neptune,
#                  m31, m42, m45,
#                  sirius, antares, deneb, betelgeuse, pollux]
#transit_bodies = [jupiter, uranus, neptune,
#                  m31, m42, m45,
#                  sirius, antares, deneb, betelgeuse, pollux]

#rising_bodies  = [mars]
#setting_bodies = [mars]
#transit_bodies = [mars]

rising_bodies  = [m31, m42, m45,
                  mercury, venus, mars, jupiter, saturn, uranus, neptune]
setting_bodies = [m31, m42, m45,
                  mercury, venus, mars, jupiter, saturn, uranus, neptune]
transit_bodies = [antares, deneb, arcturus, pollux,
                  m31, m42, m45,
                  jupiter, saturn, uranus, neptune]

