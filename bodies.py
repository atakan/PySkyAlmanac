#!/usr/bin/python
# -*- coding: utf-8 -*-
import ephem
from almanac_utils import *
from translations import t

# Objects to be plotted on the chart
# planets
mercury = PyEph_body(ephem.Mercury(), color.cmyk.BurntOrange)
venus   = PyEph_body(ephem.Venus(), color.cmyk.CornflowerBlue)
mars    = PyEph_body(ephem.Mars(), color.cmyk.Red)
jupiter = PyEph_body(ephem.Jupiter(), color.cmyk.Magenta)
saturn  = PyEph_body(ephem.Saturn(), color.cmyk.Yellow)
uranus  = PyEph_body(ephem.Uranus(), color.cmyk.SpringGreen)
neptune = PyEph_body(ephem.Neptune(), color.cmyk.ForestGreen)
# some messier objects
m1  = PyEph_body(ephem.readdb("M1,f|R,05:34:30,22:01,8.4,2000,360"), symbol='m1', tsize='tiny')
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
# some other interesting stars and systems
alcor            = PyEph_body(ephem.star('Alcor'), symbol='80 UMa', tsize='tiny')
mizar            = PyEph_body(ephem.star('Mizar'), symbol='ζ UMa', tsize='tiny')
albireo          = PyEph_body(ephem.star('Albereo'), symbol='β Cyg', tsize='tiny')
gamma_andromedae = PyEph_body(ephem.star('Almach'), symbol='γ And', tsize='tiny')

# Test of Conjunction and Appulse events
# observable, bodies, sentence = ca(obs,[mars,venus,mercury,uranus,neptune,saturn,jupiter,jupiter,sirius,betelgeuse,m13])
# print(observable,bodies,sentence)

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
