#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2021/05/30 21:46:43 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# command-line argument analysis
parser = argparse.ArgumentParser (description='reading VOTable file')
parser.add_argument ('-i', '--input', help='input VOTable file name')
args = parser.parse_args ()

# VOTable file name
file_votable = args.input

# reading VOTable
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# data
data_id        = numpy.array (table['source_id'])
data_ra        = numpy.array (table['ra'])
data_dec       = numpy.array (table['dec'])
data_parallax  = numpy.array (table['parallax'])
data_pmra      = numpy.array (table['pmra'])
data_pmdec     = numpy.array (table['pmdec'])
data_rv        = numpy.array (table['radial_velocity'])
data_b         = numpy.array (table['phot_bp_mean_mag'])
data_g         = numpy.array (table['phot_g_mean_mag'])
data_r         = numpy.array (table['phot_rp_mean_mag'])
data_br        = numpy.array (table['bp_rp'])
data_bg        = numpy.array (table['bp_g'])
data_gr        = numpy.array (table['g_rp'])
data_ra_err    = numpy.array (table['ra_error'])
data_dec_err   = numpy.array (table['dec_error'])
data_pmra_err  = numpy.array (table['pmra_error'])
data_pmdec_err = numpy.array (table['pmdec_error'])
data_p_snr     = numpy.array (table['parallax_over_error'])
data_b_snr     = numpy.array (table['phot_bp_mean_flux_over_error'])
data_g_snr     = numpy.array (table['phot_g_mean_flux_over_error'])
data_r_snr     = numpy.array (table['phot_rp_mean_flux_over_error'])

# printing header
print ("# ID, RA, Dec, parallax, proper motion in RA, proper motion in Dec")

# printing a part of data
n = 20
for i in range ( len (data_id) ):
    if (i > n):
        break
    if ( numpy.isnan (data_parallax[i]) ):
        continue
    if (data_parallax[i] < 0.0):
        continue
    print ("%s %f %+f %f %+f %+f" \
           % (data_id[i], data_ra[i], data_dec[i], data_parallax[i], \
              data_pmra[i], data_pmdec[i]) )
