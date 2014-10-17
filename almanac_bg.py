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

from almanac_utils import to_chart_coord

def make_alm_bg(bclc, begin_day_datetime, no_days, chart, obs,
        sun, sun_set, sun_rise) :
    ''' bclc: background clipped canvas'''
    # make a gradient of dark blue to black in the bg
    daycolor = color.rgb(0,82/255.0,137/255.0)
    nightcolor = color.rgb(0,0,0)
    DNcolgrad = color.lineargradient(daycolor,nightcolor)
# First try: Drawing thick lines, does not really work.
#for i in range(41) :
#    horangle = 18.0*i/40
#    obs.horizon = '-%d' % (horangle)
#    eve_twi_grad = []
#    mor_twi_grad = []
#    for doy in range(no_days) :
#        obs.date = begin_day + doy
#        eve_twi_grad.append(obs.next_setting(sun))
#        mor_twi_grad.append(obs.next_rising(sun))
#    eve_twi_gradp = event_to_path(eve_twi_grad, chart)
#    mor_twi_gradp = event_to_path(mor_twi_grad, chart)
#    clc.stroke(eve_twi_gradp,[style.linewidth(0.24),DNcolgrad.getcolor(i/40.0)])
#    clc.stroke(mor_twi_gradp,[style.linewidth(0.24),DNcolgrad.getcolor(i/40.0)])

## Second try: using rectangles for each day. Leads to a very big file
## and artifacts on screen, especially with antialiasing, hopefully fine
## when printed.
#def draw_LR_colgrad_rect(canv, LLx, LLy, W, H, colgrad, n) :
#    ''' Draw a rectangle consisting of n sub rectangles, each selecting its
#        color from the given color gradient.'''
#    for i in range(n) :
#        llx = (i+0.0)/n * W + LLx
#        lly = LLy
#        # XXX multiplication by 1.02 below is to make sure that
#        # XXX sub-rectangles overlap
#        w = 1.0/n * W * 1.02
#        h = H
#        canv.fill(path.rect(llx, lly, w, h), [colgrad.getcolor((i+0.0)/n)])
#
#day_thickness = chart.height/no_days
#for doy in range(no_days) :
#    # XXX w/o the little addition of 0.2*ephem.hour below, we would have
#    # XXX small empty triangular regions.
#    SS = to_chart_coord(sun_set[doy]-0.2*ephem.hour, chart)
#    ET = to_chart_coord(eve_twilight[doy], chart)
#    MT = to_chart_coord(mor_twilight[doy], chart)
#    SR = to_chart_coord(sun_rise[doy]+0.2*ephem.hour, chart)
## evening twilight to darkness
#    LLx = SS[0]
#    LLy = SS[1] - day_thickness/2.0
#    W = ET[0] - SS[0]
#    H = day_thickness
#    draw_LR_colgrad_rect(clc, LLx, LLy, W, H, DNcolgrad, 18)
## darkness to morning twilight
#    LLx = SR[0]
#    W = MT[0] - SR[0] # XXX note: negative width
#    draw_LR_colgrad_rect(clc, LLx, LLy, W, H, DNcolgrad, 18)



## Darkness between twilights
#rev_eve_twilight = eve_twilight[:]
#rev_eve_twilight.reverse()
#darknesspath = event_to_path_no_check(rev_eve_twilight[:] + mor_twilight[:], chart)
#darknesspath.append(path.closepath())
#clc.stroke(darknesspath, [nightcolor])
#clc.fill(darknesspath, [nightcolor])

    # Third try: Per Alp Akoğlu's request let's try to this right.
    # This way it will also be more general and easier to adapt to higher
    # latitudes where twilight never ends on some days of the year.

    gdata = []
    for doy in range(0, no_days, 10) :
        for tt in range(16*6+1) : # for 16 hours, every 10 minutes
            sun_tt = chart.ULcorn + doy + tt*ephem.minute*10
            x, y = to_chart_coord(sun_tt, chart)
            obs.date = sun_tt
            sun.compute(obs)
            z = sun.alt/ephem.degrees('-18:00:00')
            if z>1 : z=1
            if z<0 : z=0
            z = z*z # this makes the twilight more prominent
            gdata.append([x, y, z])

    # XXX I found the magic numbers below by trial error
    g = graph.graphxyz(size=1, xpos=11, ypos=16.73, xscale=12, yscale=18.31,
            projector=graph.graphxyz.parallel(-90, 90),
            x=graph.axis.linear(min=-1, max=chart.width+1, painter=None),
            y=graph.axis.linear(min=-1, max=chart.height+1, painter=None),
            z=graph.axis.linear(min=-1, max=2, painter=None))
    g.plot(graph.data.points(gdata, x=1, y=2, z=3, color=3),
           [graph.style.surface(gradient=DNcolgrad,
                                gridcolor=None,
                                backcolor=color.rgb.black)])
    bclc.insert(g)
    # the following is for the debugging the graph above
    #c.stroke(path.line(0, 0, chart.width, chart.height), [color.cmyk.Red])

def make_alm_bg_vdots(bclc, first_sunday, no_days, chart) :
    # vertical dots
    # left side is 4pm, right side is 8am. We will draw dots every 1/2 hour
    nlines = int(round((chart.URcorn-chart.ULcorn)/ephem.hour*2+1))
    xincr = chart.width/(nlines-1)
    h = chart.height
    for i in range(nlines) :
        bclc.stroke(path.line(i*xincr, 0, i*xincr, h),
                [color.cmyk.Gray, style.linestyle(style.linecap.round,
                    style.dash([0, 2.6333*366.0/no_days]))])

def make_alm_bg_hdots(bclc, first_sunday, no_days, chart) :
    # horizontal dots
    # we start with the first Sunday of the year
    for sunday in range(first_sunday, no_days, 7) :
        x1 = 0
        x2 = chart.width
        y = chart.height - (sunday * chart.height / no_days)
        bclc.stroke(path.line(x1, y, x2, y),
                [color.cmyk.Gray, style.linestyle(style.linecap.round, style.dash([0, 3.248]))])
