#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/30 18:35:53 (CST) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# command-line argument analysis
parser = argparse.ArgumentParser (description='name resolver')
parser.add_argument ('-t', '--target', help='target name')
args = parser.parse_args ()

# target object name
target = args.target

# name resolver
query_result = astroquery.simbad.Simbad.query_object (target)

# coordinate from Simbad
ra_str  = query_result['RA'][0]
dec_str = query_result['DEC'][0]

# using skycoord of astropy
coord = astropy.coordinates.SkyCoord (ra_str, dec_str, frame='icrs', \
                                      unit=(u_ha, u_deg) )
coord_str = coord.to_string (style='hmsdms')
(coord_ra_str, coord_dec_str) = coord_str.split ()
coord_ra_deg  = coord.ra.deg
coord_dec_deg = coord.dec.deg
coord_ra_rad  = coord.ra.rad
coord_dec_rad = coord.dec.rad

# printing result
print ("target: %s" % (target) )
print ("  RA  = %14s = %10.6f deg = %11.8f rad" \
       % (coord_ra_str, coord_ra_deg, coord_ra_rad) )
print ("  Dec = %14s = %+10.6f deg = %+10.8f rad" \
       % (coord_dec_str, coord_dec_deg, coord_dec_rad) )
