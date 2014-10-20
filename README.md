This program prepares a chart similar to Sky & Telescope's annual [*Skygazer's Almanac*](https://www.shopatsky.com/product/skygazers-almanac-2014-40-deg-n/calendars-and-almanacs).

The code is written in [Python](http://www.python.org/). It uses [PyX](http://pyx.sourceforge.net/) for preparing the PDF output, [PyEphem](http://rhodesmill.org/pyephem/) for astronomical calculations, and [SciPy](http://www.scipy.org/) for a simple root-finding calculation. PyEphem uses routines from [XEphem](http://www.clearskyinstitute.com/xephem/).

This is in development stage and certainly has bugs. [...] I tried to make it easy to adapt to different locations and years; in particular, the comments and the function names are in English. If you plan to port it to a different locale (location, timeframe, language etc.) please let me know. I would be more than happy to help out.

Keywords: Sky almanac -- celestial events

Atakan Gürkan <ato.gurkan@gmail.com>

##Install Dependencies
* PyEphem - `pip install pyephem`
* PyX - If using Python2, need older version of PyX like [0.12.1](http://sourceforge.net/projects/pyx/files/pyx/0.12.1/). Python3, can use current stable release. Download tarball and run `python ./setup.py install`.
* SciPy - Install full stack with `apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose`. See [here](http://www.scipy.org/install.html).

##Instructions
See `local_info.py` to see options for setting your location. There is minimal setup; you only have to change the `obs_city` field. That is, `obs_city = 'San Francisco'` or `Istanbul`.

It is of course possible your city isn't [listed](https://github.com/brandon-rhodes/pyephem/blob/master/ephem/cities.py), so in that case switch the `manually_set` flag to `True` and fill in your latitude, longitude, year, and timezone at minimum. See [this quick reference](http://rhodesmill.org/pyephem/quick.html#observers) on setting up your observer. `elevation` (m) is optional. Can also set `epoch`, `temp` and `pressure` if desired.

Turkish, English and Chinese languages are supported. In `translations.py` change `t=tr` to either `en` or `ch`.

Set `display_moon_stuff = True` or `False` for moon stuff.

#License
You can copy, modify and distribute the code under the terms of the [GNU General Public License](http://www.gnu.org/copyleft/gpl.html). See the file COPYING for more details. You can also freely distribute the end product, the chart itself. If you want to give a reference to the tool creating the chart, you can use the URL https://github.com/atakan/PySkyAlmanac
