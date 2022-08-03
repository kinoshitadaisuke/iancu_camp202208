#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/23 16:08:55 (CST) daisuke>
#

# importing astroquery module
import astroquery.jplhorizons

# querying JPL Horizons
obj = astroquery.jplhorizons.Horizons (id='134340', location='@ssb', \
                                       epochs={'start': '2021-05-24', \
                                               'stop': '2021-06-02', \
                                               'step': '1d'})

# state vector of the target object
vec = obj.vectors ()

# printing result
print ("Position of Pluto:")
for i in range ( len (vec) ):
    print ("  %s %+13.8f %+13.8f %+13.8f" \
           % (vec['datetime_str'][i], vec['x'][i], vec['y'][i], vec['z'][i]) )
