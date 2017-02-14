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

PI = atan(1)*4.0

class PyEph_body() :
    def __init__(self, pyephem_name, clr=color.cmyk.Gray,
            symbol='~', tsize='small') :
        self.body = pyephem_name
        self.color = clr
        self.symbol = symbol
        self.tsize = tsize
        self.rising = []
        self.rising_text = []
        self.transit = []
        self.transit_text = []
        self.setting = []
        self.setting_text = []
    def update_rising(self, obs) :
        self.rising.append(obs.next_rising(self.body))
    def update_transit(self, obs) :
        self.transit.append(obs.next_transit(self.body))
    def update_setting(self, obs) :
        self.setting.append(obs.next_setting(self.body))

def to_chart_coord(event_time, chart) :
    diff =  event_time - chart.ULcorn
    X = fmod(diff,1)
    if X<0.0 : X+= 1.0
    Y = floor(diff)
    X *= chart.width / (chart.URcorn - chart.ULcorn) 
    Y *= chart.height / (chart.ULcorn - chart.LLcorn)
    Y += chart.height
    return [X, Y]

def event_to_path(event, chart, do_check=True, xoffset=0.0, yoffset=0.0) :
    '''accepts an array of points representing an event, converts this
       event to a path'''
    x, y = to_chart_coord(event[0], chart)
    p = path.path(path.moveto(x,y))
    for e in event[1:] :
        old_x = x
        old_y = y
        x, y = to_chart_coord(e, chart)
        if (do_check == False or 
            (fabs(old_x - x) < chart.width/2.0  and
             fabs(old_y - y) < chart.height/2.0)) :  
            p.append(path.lineto(x+xoffset, y+yoffset))
        else :
            p.append(path.moveto(x+xoffset, y+yoffset))
    return p

#def event_to_path_no_check(event, chart) :
#    '''accepts an array of points representing an event, converts this
#       event to a path. this version does not check for big jumps in x
#       coordinate'''
#    x, y = to_chart_coord(event[0], chart)
#    p = path.path(path.moveto(x,y))
#    for e in event[1:] :
#        old_x = x
#        x, y = to_chart_coord(e, chart)
#        p.append(path.lineto(x, y))
#    return p
#
#def event_to_path_no_check_with_offset(event, chart, xoffset=0.0, yoffset=0.0) :
#    '''accepts an array of points representing an event, converts this
#       event to a path. this version does not check for big jumps in x
#       coordinate'''
#    x, y = to_chart_coord(event[0], chart)
#    p = path.path(path.moveto(x+xoffset,y+yoffset))
#    for e in event[1:] :
#        old_x = x
#        x, y = to_chart_coord(e, chart)
#        p.append(path.lineto(x+xoffset, y+yoffset))
#    return p
