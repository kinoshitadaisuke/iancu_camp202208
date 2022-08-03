#!/usr/pkg/bin/python3.9

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.time

# command-line argument analysis
parser = argparse.ArgumentParser (description='synthetic data generation')
parser.add_argument ('-o', type=str, default="out.data", \
                     help='output file name')
parser.add_argument ('-s', type=str, default="2000-01-01T12:00:00", \
                     help='start date/time of observation')
parser.add_argument ('-e', type=str, default="2000-01-02T12:00:00", \
                     help='end date/time of observation')
parser.add_argument ('-p', type=float, default=1.0, \
                     help='period in hour')
parser.add_argument ('-a', type=float, default=1.0, \
                     help='amplitude in mag')
parser.add_argument ('-m', type=float, default=20.0, \
                     help='mean magnitude')
parser.add_argument ('-u', type=float, default=0.1, \
                     help='error in mag')
parser.add_argument ('-t', type=float, default=180.0, \
                     help='time interval between exposures in sec')
args = parser.parse_args ()

# output file name
file_data = args.o

# start date/time of observation
datetime_start = args.s
t_start = astropy.time.Time (datetime_start, scale='utc')
mjd_start = t_start.mjd

# end date/time of observation
datetime_end = args.e
t_end = astropy.time.Time (datetime_end, scale='utc')
mjd_end = t_end.mjd

# period in hour
period_hr = args.p
period_day = period_hr / 24.0

# amplitude in mag
amplitude = args.a

# mean magnitude
mag_mean = args.m

# error in magnitude
mag_error = args.u

# time interval between exposures
interval_sec = args.t
interval_day = interval_sec / 86400.0

# function
def func (t, t_epoch, period_day, amplitude, mag_mean):
    mag = amplitude \
        * numpy.sin (2.0 * numpy.pi * (t - t_epoch) / period_day) \
        + mag_mean
    return (mag)

# opening file for writing
with open (file_data, 'w') as fh:
    # printing header
    header  = "# synthetic time-series data for period search\n"
    header += "#\n"
    header += "# output file name = \"%s\"\n" % file_data
    header += "# start date/time of observation = \"%s\"\n" % datetime_start
    header += "#                                  \"%s\"\n" % t_start
    header += "#                                  MJD %f\n" % mjd_start
    header += "# end date/time of observation = \"%s\"\n" % datetime_end
    header += "#                                \"%s\"\n" % t_end
    header += "#                                MJD %f\n" % mjd_end
    header += "# period in hour = %f hour\n" % period_hr
    header += "# period in day = %f day\n" % period_day
    header += "# amplitude in mag = %f mag\n" % amplitude
    header += "# mean magnitude = %f mag\n" % mag_mean
    header += "# error in magnitude = %f mag\n" % mag_error
    header += "# time interval between exposures = %f sec\n" % interval_sec
    header += "#\n"
    header += "# date/time, MJD, mag, err\n"
    header += "#\n"
    fh.write (header)

    # epoch
    t_epoch = mjd_start

    # generation of data
    t = mjd_start
    while (t < mjd_end):
        # magnitude
        mag = func (t, t_epoch, period_day, amplitude, mag_mean)
        # error
        #error = numpy.abs (numpy.random.normal (0.0, mag_error, 1))
        error = mag_error

        # date/time
        datetime = astropy.time.Time (t, format='mjd')

        # writing data
        obs = "%s %f %6.3f %6.3f\n" % (datetime.fits, t, mag, error)
        fh.write (obs)
    
        # adding interval_day to t
        t += interval_day
