#!/usr/pkg/bin/python3.9

# importing argparse module
import argparse

# importing astropy module
import astropy.timeseries
import astropy.units

# command-line argument analysis
parser = argparse.ArgumentParser (description='reading FITS files')
parser.add_argument ('files', type=str, nargs='+', help='input FITS files')
args = parser.parse_args ()

# FITS files
files_fits = args.files

# units
u_sec      = astropy.units.second
u_electron = astropy.units.electron

# processing FITS files
for file_fits in files_fits:
    # data stored in FITS file
    ts = astropy.timeseries.TimeSeries.read (file_fits, format='kepler.fits')

    # data
    data_datetime = ts['time']
    data_mjd      = ts.time.mjd
    data_flux     = ts['sap_flux'] * u_sec / u_electron
    data_err      = ts['sap_flux_err'] * u_sec / u_electron

    # printing data
    for i in range ( len (data_datetime) ):
        print (data_datetime[i], data_mjd[i], data_flux[i], data_err[i])
