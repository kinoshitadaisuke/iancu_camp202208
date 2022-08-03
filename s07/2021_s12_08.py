#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/23 18:37:08 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# file name
file_fig = '2021_s12_08.pdf'

# target list
# Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
dic_target = {
    '10':  'Sun',
    '199': 'Mercury',
    '299': 'Venus',
    '399': 'Earth',
    '499': 'Mars',
    '599': 'Jupiter',
    '699': 'Saturn',
    '799': 'Uranus',
    '899': 'Neptune',
    '999': 'Pluto'
}

# marker size
sizes   = [10, 2, 5, 5, 4, 8, 8, 6, 6, 2]
colours = ['yellow', 'blue', 'gold', 'green', 'red', \
           'orange', 'brown', 'lime', 'indigo', 'slategrey']

# number of asteroids to be plotted
n_asteroids = 1000

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'X [au]'
label_z = 'Z [au]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_z)

# axes
ax.set_xlim (-5.5, 5.5)
ax.set_ylim (-2.5, 2.5)
ax.set_aspect ('equal')
ax.grid ()

# empty numpy array to store data
asteroid_x = numpy.array ([])
asteroid_y = numpy.array ([])
    
# getting positions of asteroids
for i in range (n_asteroids):
    # querying JPL Horizons
    i_str = str (i + 1)
    if ( (i + 1) % 10 == 0):
        print ("progress: %4d / %4d" % (i + 1, n_asteroids) )
    obj = astroquery.jplhorizons.Horizons (id=i_str, id_type='smallbody', \
                                           location='@ssb', \
                                           epochs={'start': '2021-05-24', \
                                                   'stop': '2021-05-25', \
                                                   'step': '1y'})
    # state vector of the target object
    vec = obj.vectors ()

    # appending data to numpy arrays
    asteroid_x = numpy.append (asteroid_x, vec['x'][0])
    asteroid_y = numpy.append (asteroid_y, vec['z'][0])

ax.plot (asteroid_x, asteroid_y, '.', markersize=1, color='purple', \
         label='asteroids')
    
# getting positions of the Sun and planets
for i,n in enumerate (dic_target):
    # querying JPL Horizons
    obj = astroquery.jplhorizons.Horizons (id=n, id_type='majorbody', \
                                           location='@ssb', \
                                           epochs={'start': '2021-05-24', \
                                                   'stop': '2021-05-25', \
                                                   'step': '1y'})
    # state vector of the target object
    vec = obj.vectors ()

    # plotting data
    if (i < 6):
        ax.plot (vec['x'], vec['z'], marker='o', markersize=sizes[i], \
                 color=colours[i], label=dic_target[n])

# title
ax.set_title ("Inner Solar System on 24/May/2021")

# saving the plot into a file
fig.savefig (file_fig)
