#!/usr/pkg/bin/python3.9

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
parser = argparse.ArgumentParser (description='making folded lightcurve')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.pdf", \
                     help='output figure file name')
parser.add_argument ('-p', type=float, default=1.0, \
                     help='period in hr')
args = parser.parse_args ()


# data file name
file_data = args.i

# output file name
file_fig = args.o

# assumed period (day)
p_assumed = args.p / 24.0

# empty numpy arrays for storing data
data_mjd   = numpy.array ([])
data_mag   = numpy.array ([])
data_err   = numpy.array ([])
data_phase = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
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
        data_mjd   = numpy.append (data_mjd, mjd)
        data_mag   = numpy.append (data_mag, mag)
        data_err   = numpy.append (data_err, err)

        # calculation of phase using assumed period
        phase = (mjd - data_mjd[0]) / p_assumed
        phase -= int (phase)
        data_phase = numpy.append (data_phase, phase)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Phase'
label_y = 'Magnitude [mag]'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# plotting data
ax.get_xaxis ().get_major_formatter ().set_useOffset (False)
ax.invert_yaxis ()
ax.errorbar (data_phase, data_mag, yerr=data_err, fmt='b.', \
             markersize=5, ecolor='black', capsize=0, \
             label='folded lightcurve')
ax.errorbar (data_phase + 1.0, data_mag, yerr=data_err, fmt='b.', \
             markersize=5, ecolor='black', capsize=0)
ax.legend (bbox_to_anchor=(1.0, 1.12), loc='upper right')

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
