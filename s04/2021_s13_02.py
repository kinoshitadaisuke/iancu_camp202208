#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/30 19:15:19 (CST) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.units
import astropy.coordinates
import astropy.io.fits

# importing astroquery module
import astroquery.simbad
import astroquery.skyview

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# list of surveys
list_surveys = ['DSS2 Blue', 'DSS2 Red', 'DSS2 IR']

# command-line argument analysis
parser = argparse.ArgumentParser (description='FITS file downloading')
parser.add_argument ('-s', '--survey', choices=list_surveys, \
                     default='DSS2 Red', help='choice of survey')
parser.add_argument ('-t', '--target', help='target name')
parser.add_argument ('-f', '--fov', type=float, help='field-of-view in arcmin')
parser.add_argument ('-o', '--output', help='name of output file')
args = parser.parse_args ()

# target object name
survey      = args.survey
target      = args.target
fov_arcmin  = args.fov
file_output = args.output

# field-of-view
fov_arcsec = fov_arcmin * 60.0
fov_pixel  = int (fov_arcsec)

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

# getting a list of images
list_image = astroquery.skyview.SkyView.get_image_list (position=coord, \
                                                        survey=survey)

print ("images =", list_image)

# getting images
images = astroquery.skyview.SkyView.get_images (position=coord, \
                                                survey=survey, \
                                                pixels=fov_pixel)

# image
image  = images[0]
header = image[0].header
data   = image[0].data
print (image.info ())

# writing FITS file
print ("Writing a FITS file \"%s\"..." % (file_output) )
hdu = astropy.io.fits.PrimaryHDU (data=data, header=header)
hdu.writeto (file_output)
print ("Done!")
