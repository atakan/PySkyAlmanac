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

from math import floor, fmod, fabs, atan2, atan, asin, sqrt, sin, cos
import datetime, calendar, ephem, pytz, pyx
from datetime import timedelta as TD
from pyx import path, canvas, color, style, text, graph
from scipy import optimize

from almanac_utils import *

mooncolorlight = color.rgb(0.6235294,0.6823529,0.827451)
mooncolordark = color.rgb(0.3450980,0.3764706,0.458823)

def S_of_R(R) :
    return (R*R*asin(1.0/R) - 1.0*sqrt(R*R-1.0))/ (PI)

def R_of_S(S) :
    def func(x) :
        return S_of_R(x)-S
    return optimize.bisect(func, 1.0000001, 100.0)

def first_quarter_moon(r, cx, cy) :
    p = path.path(path.moveto(cx, cy))
    p.append(path.arc(cx, cy, r, -90, 90))
    p.append(path.closepath())
    return p
def last_quarter_moon(r, cx, cy) :
    p = path.path(path.moveto(cx, cy))
    p.append(path.arc(cx, cy, r, 90, -90))
    p.append(path.closepath())
    return p

def waxing_moon(X, r, cx, cy) :
    '''draws a waxing moon figure, used for moonset.'''
    p = path.path(path.moveto(cx, cy-r))
    p.append(path.arc(cx, cy, r, -90, 90))
    if X>0.5 :
        R = R_of_S(X-0.5)*r
        theta = asin(r/R)*180/PI
        moon_arc_p = path.arc(cx+sqrt(R*R-r*r), cy, R, 180-theta, 180+theta)
    else :
        R = R_of_S(0.5-X)*r
        theta = asin(r/R)*180/PI
        moon_arc_p = path.arc(cx-sqrt(R*R-r*r), cy, R, -theta, theta)
        p = path.path.reversed(p)
    p.append(moon_arc_p)
    return p

def waning_moon(X, r, cx, cy) :
    '''draws a waning moon figure, used for moonrise.'''
    p = path.path(path.moveto(cx, cy+r))
    p.append(path.arc(cx, cy, r, 90, -90))
    if X>0.5 :
        R = R_of_S(X-0.5)*r
        theta = asin(r/R)*180/PI
        moon_arc_p = path.arc(cx-sqrt(R*R-r*r), cy, R, -theta, theta)
    else :
        R = R_of_S(0.5-X)*r
        theta = asin(r/R)*180/PI
        moon_arc_p = path.arc(cx+sqrt(R*R-r*r), cy, R, 180-theta, 180+theta)
        p = path.path.reversed(p)
    p.append(moon_arc_p)
    return p

def make_moon_stuff(outer_canv, inner_canv, begin_day, no_days, chart,
        obs):
    small_moon_rad = 0.12
    large_moon_rad = 0.16
    moon = ephem.Moon()
    moon2 = ephem.Moon()
    for doy in range(no_days) :
        obs.date = begin_day + doy
        mpc = obs.date + 0.5 # moon phase check
        moon_set = obs.next_setting(moon)
        moon2.compute(moon_set)
        X = moon2.moon_phase
        # Waxing moon (moonsets)
        x, y = to_chart_coord(moon_set, chart)
        if (fabs(ephem.next_full_moon(mpc) - mpc) < 0.5 or
            fabs(ephem.previous_full_moon(mpc) - mpc) < 0.5) :
            # full moon
            outer_canv.stroke(path.circle(x,y,large_moon_rad),[mooncolorlight,pyx.deco.filled([mooncolorlight])])
        elif ((X < 0.55 and X > 0.45) or 
              fabs(ephem.next_first_quarter_moon(mpc) - mpc) < 0.5 or
              fabs(ephem.previous_first_quarter_moon(mpc) - mpc) < 0.5) :
            # first quarter
            outer_canv.stroke(first_quarter_moon(large_moon_rad, x,y),[mooncolordark,pyx.deco.filled([mooncolordark])])
        elif (fabs(ephem.next_new_moon(mpc) - mpc) < 0.5 or
              fabs(ephem.previous_new_moon(mpc) - mpc) < 0.5):
            # new moon
            outer_canv.stroke(path.circle(x,y,large_moon_rad),[mooncolorlight,pyx.deco.filled([mooncolordark])])
        else :
            inner_canv.fill(waxing_moon(X, small_moon_rad, x, y),
                    [style.linejoin.bevel,mooncolordark])
        # Waning moon (moonrises)
        moon_rise = obs.next_rising(moon)
        moon2.compute(moon_rise)
        X = moon2.moon_phase
        x, y = to_chart_coord(moon_rise, chart)
        if (fabs(ephem.next_full_moon(mpc) - mpc) < 0.5 or
            fabs(ephem.previous_full_moon(mpc) - mpc) < 0.5) :
            # full moon
            outer_canv.stroke(path.circle(x,y,large_moon_rad),[mooncolorlight,pyx.deco.filled([mooncolorlight])])
        elif ((X < 0.55 and X > 0.45) or 
              fabs(ephem.next_last_quarter_moon(mpc) - mpc) < 0.5 or
              fabs(ephem.previous_last_quarter_moon(mpc) - mpc) < 0.5) :
            # last quarter
            outer_canv.stroke(last_quarter_moon(large_moon_rad, x,y),[mooncolorlight,pyx.deco.filled([mooncolorlight])])
        elif (fabs(ephem.next_new_moon(mpc) - mpc) < 0.5 or
              fabs(ephem.previous_new_moon(mpc) - mpc) < 0.5):
            # new moon
            outer_canv.stroke(path.circle(x,y,large_moon_rad),[mooncolorlight,pyx.deco.filled([mooncolordark])])
        else :
            inner_canv.fill(waning_moon(X, small_moon_rad, x, y),
                    [style.linejoin.bevel,mooncolorlight])

def make_moon_key(canv, chart) :
    large_moon_rad = 0.16
    small_moon_rad = 0.12
    x = 0.0
    y = -1.8
    canv.fill(path.rect(x, y, chart.width, 1.0), 
            [color.rgb(0.0, 0.0, 0.0)])
    for i in range(8) :
        X = 1.0-(i+1.0)/9.0
        canv.fill(waning_moon(X, small_moon_rad, x+(i+4.0)/4.0, -1.3),
                    [style.linejoin.bevel,mooncolorlight])
    canv.text(x+1.8, -1.1,
              r'{\footnotesize\sffamily Küçülen Ay}',
              [text.halign.center,text.valign.baseline,mooncolorlight])
    canv.text(x+1.8, -1.7,
              r"{\scriptsize\sffamily (Ay'ın doğuş zamanları)}",
              [text.halign.center,text.valign.baseline,mooncolorlight])
    for i in range(8) :
        X = (i+1.0)/9.0
        canv.fill(waxing_moon(X, small_moon_rad, x+(i+4.0)/4.0+3.0, -1.3),
                    [style.linejoin.bevel,mooncolordark])
    canv.text(x+1.8+3.0, -1.1,
              r'{\footnotesize\sffamily Büyüyen Ay}',
              [text.halign.center,text.valign.baseline,mooncolordark])
    canv.text(x+1.8+3.0, -1.7,
              r"{\scriptsize\sffamily (Ay'ın batış zamanları)}",
              [text.halign.center,text.valign.baseline,mooncolordark])
    # new moon, first quarter
    # full moon,  last quarter
    canv.stroke(path.circle(x+8.5,-1.1,large_moon_rad),[mooncolorlight,pyx.deco.filled([mooncolordark])])
    canv.text(x+8.25, -1.2, r'{\footnotesize\sffamily Yeni ay}',
            [text.halign.right,text.valign.baseline, mooncolordark])
    canv.stroke(first_quarter_moon(large_moon_rad, x+8.9,-1.1),[mooncolordark,pyx.deco.filled([mooncolordark])])
    canv.text(x+9.25, -1.2, r'{\footnotesize\sffamily İlk dördün}',
            [text.halign.left,text.valign.baseline, mooncolordark])
    canv.stroke(path.circle(x+8.5,-1.5,large_moon_rad),[mooncolorlight,pyx.deco.filled([mooncolorlight])])
    canv.text(x+8.25, -1.6, r'{\footnotesize\sffamily Dolunay}',
            [text.halign.right,text.valign.baseline, mooncolorlight])
    canv.stroke(last_quarter_moon(large_moon_rad, x+8.9,-1.5),[mooncolorlight,pyx.deco.filled([mooncolorlight])])
    canv.text(x+9.25, -1.6, r'{\footnotesize\sffamily Son dördün}',
            [text.halign.left,text.valign.baseline, mooncolorlight])
