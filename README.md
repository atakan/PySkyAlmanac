This is program that prepares a chart similar to Sky & Telescope's
annual [*Skygazer's Almanac*](http://www.shopatsky.com/product/Skygazers-Almanac-2011-Wall-Chart/].

The code is written in Python. It uses
[PyX](http://pyx.sourceforge.net/) for preparing the PDF output,
[PyEphem](http://rhodesmill.org/pyephem/) for astronomical calculations,
and [SciPy](http://www.scipy.org/) for a simple root-finding calculation.

This is in development stage and certainly has bugs. In addition, the
code is for Ankara and 2010. I tried to make it easy to adapt to
different locations and years, in particular the comments and the
function names are in Engligh. If you plan to port it to a different
locale (location, timeframe, language etc.) please let me know. I would
be more than happy to help out.

Keywords: Sky almanac -- celestial events

Atakan Gürkan <ato.gurkan@gmail.com>

