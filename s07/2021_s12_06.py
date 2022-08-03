#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/23 17:23:18 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# file name
file_fig = '2021_s12_06.pdf'

# target list
# Earth, Mars
list = ['399', '499']

# start date
date_start = '2010-01-01'

# end date
date_end   = '2030-01-01'

# step
step = '10d'

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Time [year]'
label_y = 'Distance between Earth and Mars [au]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# axes
ax.set_ylim (0, 3.5)
ax.grid ()

# getting positions of Earth and Mars
earth = astroquery.jplhorizons.Horizons (id=list[0], id_type='majorbody', \
                                         location='@ssb', \
                                         epochs={'start': date_start, \
                                                 'stop': date_end, \
                                                 'step': step})
# state vector of the target object
vec_earth = earth.vectors ()

mars = astroquery.jplhorizons.Horizons (id=list[1], id_type='majorbody', \
                                        location='@ssb', \
                                        epochs={'start': date_start, \
                                                'stop': date_end, \
                                                'step': step})
# state vector of the target object
vec_mars = mars.vectors ()

# date/time
datetime   = astropy.time.Time (vec_earth['datetime_jd'], format='jd')
datetime64 = numpy.array (datetime.isot, dtype='datetime64')

# distance between Earth and Mars
delta_x = vec_earth['x'] - vec_mars['x']
delta_y = vec_earth['y'] - vec_mars['y']
delta_z = vec_earth['z'] - vec_mars['z']
dist    = numpy.sqrt (delta_x**2 + delta_y**2 + delta_z**2)

# plotting data
ax.plot (datetime64, dist, 'r-', label='Distance between Earth and Mars')

# showing legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig)
