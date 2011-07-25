#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

from math import floor, fmod, fabs, atan2, atan, asin, sqrt, sin, cos
import datetime, calendar, ephem, pytz, pyx
from datetime import timedelta as TD
from pyx import path, canvas, color, style, text, graph
from scipy import optimize

def to_chart_coord(event_time, chart) :
    diff =  event_time - chart.ULcorn
    X = fmod(diff,1)
    if X<0.0 : X+= 1.0
    Y = floor(diff)
    X *= chart.width / (chart.URcorn - chart.ULcorn) 
    Y *= chart.height / (chart.ULcorn - chart.LLcorn)
    Y += chart.height
    return [X, Y]
