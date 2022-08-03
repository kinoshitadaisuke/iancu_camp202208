#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/30 21:39:49 (CST) daisuke>
#

# importing argparse
import argparse

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad
import astroquery.gaia

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# command-line argument analysis
parser = argparse.ArgumentParser (description='Gaia Catalogue downloading')
parser.add_argument ('-t', '--target', help='target name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-r', '--radius', type=float, \
                     help='radius of search in arcmin')
args = parser.parse_args ()

# parameters
target        = args.target
file_output   = args.output
radius_arcmin = args.radius
radius_deg    = radius_arcmin / 60.0

# units
u_deg = astropy.units.deg
u_ha  = astropy.units.hourangle
u_arcmin = astropy.units.arcmin

# name resolver
result_simbad = astroquery.simbad.Simbad.query_object (target)

# coordinate from Simbad
obj_ra  = result_simbad['RA'][0]
obj_dec = result_simbad['DEC'][0]

# using skycoord of astropy
coord = astropy.coordinates.SkyCoord (obj_ra, obj_dec, frame='icrs', \
                                      unit=(u_ha, u_deg) )
coord_str = coord.to_string (style='hmsdms')
(coord_ra_str, coord_dec_str) = coord_str.split ()
coord_ra_deg  = coord.ra.deg
coord_dec_deg = coord.dec.deg
coord_ra_rad  = coord.ra.rad
coord_dec_rad = coord.dec.rad

# printing target
print ("target: %s" % (target) )
print ("  RA  = %14s = %10.6f deg = %11.8f rad" \
       % (coord_ra_str, coord_ra_deg, coord_ra_rad) )
print ("  Dec = %14s = %+10.6f deg = %+10.8f rad" \
       % (coord_dec_str, coord_dec_deg, coord_dec_rad) )

# command for database query
query_p = "POINT('ICRS',gaiadr2.gaia_source.ra,gaiadr2.gaia_source.dec)"
query_c = "CIRCLE('ICRS',%f,%f,%f)" % (coord_ra_deg, coord_dec_deg, radius_deg)
query   = "SELECT * from gaiadr2.gaia_source WHERE CONTAINS(%s,%s)=1;" \
    % (query_p, query_c)

# sending a job to Gaia database
job = astroquery.gaia.Gaia.launch_job_async (query, dump_to_file=True, \
                                             output_file=file_output)
print (job)

# getting results
results = job.get_results ()

# printing results
print (results)
