This program prepares a chart similar to Sky & Telescope's annual [*Skygazer's Almanac*](https://www.shopatsky.com/product/skygazers-almanac-2014-40-deg-n/calendars-and-almanacs).

The code is written in [Python](http://www.python.org/). It uses [PyX](http://pyx.sourceforge.net/) for preparing the PDF output, [PyEphem](http://rhodesmill.org/pyephem/) for astronomical calculations, and [SciPy](http://www.scipy.org/) for a simple root-finding calculation. PyEphem uses routines from [XEphem](http://www.clearskyinstitute.com/xephem/).

This is in development stage and certainly has bugs. We're more than happy to help anyone trying to port this to a different locale (location, timeframe, language etc.).

Keywords: Sky almanac, celestial events, astronomy

##Install Dependencies
* PyEphem - `pip install pyephem`
* PyX - If using Python2, need older version of PyX like [0.12.1](http://sourceforge.net/projects/pyx/files/pyx/0.12.1/). Python3, can use current stable release. Download tarball and run `python ./setup.py install`.
* SciPy - Install full stack with `apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose`. See [here](http://www.scipy.org/install.html).

**Optional**
* [git](http://git-scm.com) - `apt-get install git` - Git is assumed to have been installed. I don't know why you wouldn't have it :). Necessary if hosting your own city's almanac and want to link to it in the chart. See [skyalmanac.py#L406](https://github.com/digitalvapor/PySkyAlmanac/blob/master/skyalmanac.py#L406).
* [goslate](http://pythonhosted.org/goslate/) - `pip install goslate` - used in [translations.py](https://github.com/digitalvapor/PySkyAlmanac/blob/master/translations.py). (experimental)

##Instructions
See `local_info.py` to see options for setting your location. There is minimal setup; you only have to change the `obs_city` field. That is, `obs_city = 'San Francisco'` or `Istanbul`.

It is of course possible your city isn't [listed](https://github.com/brandon-rhodes/pyephem/blob/master/ephem/cities.py), so in that case switch the `manually_set` flag to `True` and fill in your latitude, longitude, year, and timezone at minimum. Set `use_your_timezone` to False if you are generating for a different city than where you are. See [this quick reference](http://rhodesmill.org/pyephem/quick.html#observers) on setting up your observer. `elevation` (m) is optional. Can also set `epoch`, `temp` and `pressure` if desired.

Turkish, English, Chinese, and German languages are supported. In `translations.py` change `t=en` to either `tr`, `ch` or `de`.

Options:
```
equation_of_time = False  # plot equation of time
display_moon_stuff = True # for moon stuff
display_bg = True         # display night gradient
display_dst_msg = True    # prints a note on accounting for DST
use_city = True           # use a city from the modest pyephem database
use_today = True          # use the year based on today
use_your_timezone = True  # are you printing for your timezone
output_pdf = True
output_png = True
png_transparency = False
```

###Plotting Astronomical Catalog Objects
You can plot [Messier](https://en.wikipedia.org/wiki/List_of_Messier_objects) and other objects from astronomical catalogs as follows. There are plenty of catalogs like NGC. For this example, Xephem has a [subset of astronomical catalogs](http://web.mit.edu/outland/share/lib/xephem/edb/). To add the Ring Nebula, I will look at [messier.edb](http://web.mit.edu/outland/share/lib/xephem/edb/Messier.edb) and copy `M57 NGC6720,f|P,18:53:36,33:02,9,2000,86` into [local_info.py](https://github.com/digitalvapor/PySkyAlmanac/blob/master/local_info.py) as `m57 = PyEph_body(ephem.readdb("M57,f|P,18:53:36,33:02,9,2000,86"), symbol='m57', tsize='tiny')`. In addition, I'm also going to plot [the Crab Nebula](https://en.wikipedia.org/wiki/Crab_Nebula) (M1) and [the Owl Nebula](https://en.wikipedia.org/wiki/Owl_Nebula) (M97) to keep the format in the key. You don't have to add items to the key, but I'm going to mention it because if you would like to add items that people can use in other languages, modify [translations.py](https://github.com/digitalvapor/PySkyAlmanac/blob/master/translations.py) to include the new object. For example, with the Ring Nebula, I added `'ring_nebula':'Ring Nebula',` to the english dictionary, then in the other dictionaries (Turkish and Chinese at the time of writing) I added `'ring_nebula':en['ring_nebula'],`. Later, I'll use google.translate or try to find somebody to translate. Then add to key with

```
c.text(llx+15.5, -1.4, r'{\footnotesize\sffamily M57: '+t['ring_nebula']+'}',
    [text.halign.left,text.valign.baseline,color.cmyk.Gray])
```

#Fork
If you are generating this sky chart, please consider forking the repository and using [github pages](https://pages.github.com/) to host your city's custom sky almanac.

* [Ankara](https://atakan.github.io/PySkyAlmanac/)
* [San Francisco](https://digitalvapor.github.io/PySkyAlmanac/)

My primary aim in [this fork](https://github.com/digitalvapor/PySkyAlmanac) has been to change out all of the hard-coded Ankara values so that any location generates with a clean format. Many thanks to [atakan](https://github.com/atakan/PySkyAlmanac) for creating such a great tool!! If you want to give a reference to the tool creating the chart, you can use the URL https://github.com/atakan/PySkyAlmanac. If you are curious on what is on my to-do list please check out [my pull request](https://github.com/atakan/PySkyAlmanac/pull/1) and don't hesistate to [use the issue tracker](https://github.com/digitalvapor/PySkyAlmanac/issues) for this fork, or [atakan's](https://github.com/atakan/PySkyAlmanac/issues). There are definitely bugs, sorry :)

#License
You can copy, modify and distribute the code under the terms of the [GNU General Public License](http://www.gnu.org/copyleft/gpl.html). See the file COPYING for more details. You can also freely distribute the end product, the chart itself.
