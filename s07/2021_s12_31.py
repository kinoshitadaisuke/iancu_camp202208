#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/23 23:59:21 (CST) daisuke>
#

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing rebound module
import rebound

# MPC's orbital elements file
file_mpcorb = 'mpcorb.dat'

# simulation file to be generated
file_sim = 'iss.bin'

majorbody = {
    'Sun':     '10',
    'Mercury': '1',
    'Venus':   '2',
    'Earth':   '3',
    'Mars':    '4',
    'Jupiter': '5',
    'Saturn':  '6',
    'Uranus':  '7',
    'Neptune': '8',
}

# number of asteroids to process
n_asteroids = 3000

# epoch of orbital elements
# K20CH = 2020-Dec-17
# if the epoch is not K20CH, then change following line
t_epoch = '2020-12-17 00:00'

# construction of a simulation
sim = rebound.Simulation ()

# adding major bodies
for name in majorbody.keys ():
    sim.add (majorbody[name], date=t_epoch)

# dictionary to store orbital elements
dic_elements = {}

# opening file
with open (file_mpcorb, 'r') as fh:
    # flag
    data_line = 'NO'
    # reading file
    for line in fh:
        if (data_line == 'YES'):
            # number (or provisional designation)
            number = line[0:7]
            # epoch
            epoch = line[20:25]
            # mean anomaly
            M = float (line[26:35])
            M_rad = numpy.deg2rad (M)
            # argument of perihelion
            peri = float (line[37:46])
            peri_rad = numpy.deg2rad (peri)
            # longitude of ascending node
            node = float (line[48:57])
            node_rad = numpy.deg2rad (node)
            # inclination
            i = float (line[59:68])
            i_rad = numpy.deg2rad (i)
            # eccentricity
            e = float (line[70:79])
            # semimajor axis
            a = float (line[92:103])

            # adding data to the dictionary
            dic_elements[number] = {}
            dic_elements[number]['a'] = a
            dic_elements[number]['e'] = e
            dic_elements[number]['i'] = i_rad
            dic_elements[number]['peri'] = peri_rad
            dic_elements[number]['node'] = node_rad
            dic_elements[number]['M'] = M_rad

            # when finish reading expected number of asteroid data, then break
            if (int (number) == n_asteroids):
                break
        # if the line starts with '----------'
        if (line[:10] == '----------'):
            # set the flag to 'YES'
            data_line = 'YES'
            continue

# processing each asteroid orbit
for number in sorted (dic_elements.keys ()):
    # adding an asteroid
    sim.add (m=0.0, \
             a=dic_elements[number]['a'], \
             e=dic_elements[number]['e'], \
             inc=dic_elements[number]['i'], \
             omega=dic_elements[number]['peri'], \
             Omega=dic_elements[number]['node'], \
             M=dic_elements[number]['M'], \
             date=t_epoch)

# saving simulation to a file
sim.save (file_sim)
