#!/usr/pkg/bin/python3.9

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.timeseries

# command-line argument analysis
parser = argparse.ArgumentParser (description='Lomb-Scargle periodogram')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.data", \
                     help='output data file name')
parser.add_argument ('-a', type=float, default=0.01, \
                     help='minimum trial period in min')
parser.add_argument ('-b', type=float, default=14400.0, \
                     help='maximum trial period in min')
parser.add_argument ('-n', type=int, default=30, \
                     help='samples per peak for frequency grid spacing')
args = parser.parse_args ()

# data file name
file_in = args.i

# output file name
file_out = args.o

# minimum trial period
per_min_min  = args.a
per_min_hr   = per_min_min / 60.0
per_min_day  = per_min_min / 1440.0
freq_max_day = 1.0 / per_min_day

# maximum trial period
per_max_min  = args.b
per_max_hr   = per_max_min / 60.0
per_max_day  = per_max_min / 1440.0
freq_min_day = 1.0 / per_max_day

# samples per peak
n = args.n

# empty numpy arrays for storing data
data_mjd = numpy.array ([])
data_mag = numpy.array ([])
data_err = numpy.array ([])

# opening file for reading
with open (file_in, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (datetime_str, mjd_str, mag_str, err_str) = line.split ()
        # conversion from string into float
        mjd = float (mjd_str)
        mag = float (mag_str)
        err = float (err_str)
        # appending the data at the end of numpy arrays
        data_mjd = numpy.append (data_mjd, mjd)
        data_mag = numpy.append (data_mag, mag)
        data_err = numpy.append (data_err, err)

# Lomb-Scargle periodogram
freq, power = astropy.timeseries.LombScargle (data_mjd, data_mag, data_err) \
                                .autopower (minimum_frequency=freq_min_day, \
                                            maximum_frequency=freq_max_day, \
                                            samples_per_peak=n)

# opening file for writing
with open (file_out, 'w') as fh_out:
    # writing header to file
    header  = "# result of period search by Lomb-Scargle periodogram\n"
    header += "# using astropy.timeseries.LombScargle ()\n"
    header += "#\n"
    header += "# input file = \"%s\"\n" % file_in
    header += "# output file = \"%s\"\n" % file_out
    header += "# samples per peak = %d\n" % n
    header += "# minimum period = %f hr\n" % per_min_hr
    header += "# maximum period = %f hr\n" % per_max_hr
    header += "#\n"
    header += "# frequency in cycle day^-1, period in day, period in hour, "
    header += "period in min, power\n"
    header += "#\n"
    fh_out.write (header)

    # writing data to file
    for i in range ( len (freq) ):
        record = "%.10f %.10f %.10f %.10f %.10f\n" \
            % (freq[i], 1.0 / freq[i], 1.0 / freq[i] * 24.0, \
               1.0 / freq[i] * 1440, power[i])
        fh_out.write (record)
