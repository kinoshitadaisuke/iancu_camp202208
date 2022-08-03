#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/24 11:50:20 (CST) daisuke>
#

# importing numpy module
import numpy

# MPC's orbital elements file
file_mpcorb = 'mpcorb.dat'

# number of asteroids to process
n_asteroids = 1000

# dictionary to store orbital elements
dic_elements = {}

n_jt = 0

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
            # orbit type
            orbit_type = line[161:165]

            # adding data to the dictionary if Jovian Trojan asteroid
            if (orbit_type == '0009'):
                dic_elements[number] = {}
                dic_elements[number]['a'] = a
                dic_elements[number]['e'] = e
                dic_elements[number]['i'] = i_rad
                dic_elements[number]['peri'] = peri_rad
                dic_elements[number]['node'] = node_rad
                dic_elements[number]['M'] = M_rad
                # increment
                n_jt += 1

            # when finish reading expected number of asteroid data, then break
            if (n_jt >= n_asteroids):
                break
        # if the line starts with '----------'
        if (line[:10] == '----------'):
            # set the flag to 'YES'
            data_line = 'YES'
            continue
            
for number in sorted (dic_elements.keys ()):
    print ("%s %f %f %f %f %f %f" % (number, \
                                     dic_elements[number]['a'], \
                                     dic_elements[number]['e'], \
                                     dic_elements[number]['i'], \
                                     dic_elements[number]['peri'], \
                                     dic_elements[number]['node'], \
                                     dic_elements[number]['M'], \
                                     ) )
