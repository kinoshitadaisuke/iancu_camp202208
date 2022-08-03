#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/23 16:42:48 (CST) daisuke>
#

# importing astroquery module
import astroquery.jplhorizons

# target list
# Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
list = ['10', '199', '299', '399', '499', '599', '699', '799', '899', '999']

# names
names = {
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

# printing header
print ("Positions of the Sun and planets on 2021-05-24 00:00 (UT):")

# getting positions of the Sun and planets
for i in range ( len (list) ):
    # querying JPL Horizons
    obj = astroquery.jplhorizons.Horizons (id=list[i], id_type='majorbody', \
                                           location='@ssb', \
                                           epochs={'start': '2021-05-24', \
                                                   'stop':  '2021-05-25', \
                                                   'step':  '1y'})
    # state vector of the target object
    vec = obj.vectors ()

    # printing position
    print ("  %10s %+13.8f %+13.8f %+13.8f" \
           % (names[list[i]], vec['x'][0], vec['y'][0], vec['z'][0]) )
