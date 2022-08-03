#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/23 16:39:10 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astroquery module
import astroquery.jplhorizons

# querying JPL Horizons
obj_sun   = astroquery.jplhorizons.Horizons (id_type='majorbody', id='399', \
                                             location='@ssb', \
                                             epochs={'start': '2021-05-24', \
                                                     'stop': '2022-05-24', \
                                                     'step': '30d'})
obj_pluto = astroquery.jplhorizons.Horizons (id_type='smallbody', id='Pluto', \
                                             location='@ssb', \
                                             epochs={'start': '2021-05-24', \
                                                     'stop': '2022-05-24', \
                                                     'step': '30d'})

# state vector of the target object
vec_sun   = obj_sun.vectors ()
vec_pluto = obj_pluto.vectors ()

# printing result
print ("Distance between the Earth and Pluto:")
for i in range ( len (vec_sun) ):
    datetime        = vec_sun['datetime_str'][i]
    datetime_fields = datetime.split ()
    dx   = vec_sun['x'][i] - vec_pluto['x'][i]
    dy   = vec_sun['y'][i] - vec_pluto['y'][i]
    dz   = vec_sun['z'][i] - vec_pluto['z'][i]
    dist = numpy.sqrt (dx**2 + dy**2 + dz**2)
    print ("  %s %+6.3f %+6.3f %+6.3f %+6.3f %+6.3f %+6.3f %6.3f" \
           % (datetime_fields[1], \
              vec_sun['x'][i], vec_sun['y'][i], vec_sun['z'][i], \
              vec_pluto['x'][i], vec_pluto['y'][i], vec_pluto['z'][i], \
              dist) )
