This is program that prepares a chart similar to Sky & Telescope's
annual [*Skygazer's Almanac*](http://www.shopatsky.com/product/Skygazers-Almanac-2011-Wall-Chart/).

The code is written in [Python](http://www.python.org/). It uses
[PyX](http://pyx.sourceforge.net/) for preparing the PDF output,
[PyEphem](http://rhodesmill.org/pyephem/) for astronomical calculations,
and [SciPy](http://www.scipy.org/) for a simple root-finding calculation.
PyEphem uses routines from
[XEphem](http://www.clearskyinstitute.com/xephem/).

You can copy, modify and distribute the code under the terms of the
[GNU General Public License](http://www.gnu.org/copyleft/gpl.html). See
the file COPYING for more details. You can also freely distribute
the end product, the chart itself. If you want to give a reference to the
tool creating the chart, you can use the URL
https://github.com/atakan/PySkyAlmanac

This is in development stage and certainly has bugs. In addition, the
code is for Ankara and 2012. I tried to make it easy to adapt to
different locations and years; in particular, the comments and the
function names are in English. If you plan to port it to a different
locale (location, timeframe, language etc.) please let me know. I would
be more than happy to help out.

Keywords: Sky almanac -- celestial events

Atakan Gürkan <ato.gurkan@gmail.com>

##Install Dependencies
* PyEphem - `pip install pyephem`
* PyX - If using Python2, need older version of PyX like [0.12.1](http://sourceforge.net/projects/pyx/files/pyx/0.12.1/). Python3, can use current stable release. Download tarball and run `python ./setup.py install`.
* SciPy - Install full stack with `apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose`. See [here](http://www.scipy.org/install.html).
