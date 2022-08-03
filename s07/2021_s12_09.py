#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/24 10:10:16 (CST) daisuke>
#

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing rebound module
import rebound

# simulation file to be generated
file_sim = 'comets.bin'

# major bodies
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
    'Pluto':   '9',
}

# minor bodies
minorbody = {
    '1P/Halley':                 'DES=1P; CAP',
    '2P/Encke':                  'DES=2P; CAP',
    '8P/Tuttle':                 'DES=8P; CAP',
    '21P/Giacobini-Zinner':      'DES=21P; CAP',
    '29P/Schwassmann-Wachmann':  'DES=29P; CAP',
    '55P/Tempel-Tuttle':         'DES=55P; CAP',
    '67P/Churyumov-Gerasimenko': 'DES=67P; CAP',
}

# epoch of orbital elements
# K20CH = 2020-Dec-17
# if the epoch is not K20CH, then change following line
t_epoch = '2020-12-17 00:00'

# construction of a simulation
sim = rebound.Simulation ()

# adding major bodies
for name in majorbody.keys ():
    sim.add (majorbody[name], date=t_epoch, hash=name)

# adding minor bodies
for name in minorbody.keys ():
    sim.add (minorbody[name], date=t_epoch, hash=name)

# saving simulation to a file
sim.save (file_sim)
