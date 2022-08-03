#!/usr/pkg/bin/python3.9

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
parser = argparse.ArgumentParser (description='plotting power spectrum')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.pdf", \
                     help='output figure file name')
parser.add_argument ('-a', type=float, default=0.0, \
                     help='minimum period to be plotted in day')
parser.add_argument ('-b', type=float, default=100.0, \
                     help='maximum period to be plotted in day')
args = parser.parse_args ()

# data file name
file_data = args.i

# output file name
file_fig = args.o

# minimum period to be plotted
per_min_day = args.a

# maximum period to be plotted
per_max_day = args.b

# empty numpy arrays for storing data
data_freq    = numpy.array ([])
data_per_day = numpy.array ([])
data_per_hr  = numpy.array ([])
data_per_min = numpy.array ([])
data_power   = numpy.array ([])

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
        (freq_str, per_day_str, per_hr_str, per_min_str, power_str) \
            = line.split ()
        # conversion from string into float
        freq    = float (freq_str)
        per_day = float (per_day_str)
        per_hr  = float (per_hr_str)
        per_min = float (per_min_str)
        power   = float (power_str)
        # appending the data at the end of numpy arrays
        if ( (per_day >= per_min_day) and (per_day <= per_max_day) ):
            data_freq    = numpy.append (data_freq, freq)
            data_per_day = numpy.append (data_per_day, per_day)
            data_per_hr  = numpy.append (data_per_hr, per_hr)
            data_per_min = numpy.append (data_per_min, per_min)
            data_power   = numpy.append (data_power, power)

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# labels
label_x = 'Period [day]'
label_y = 'Power'
ax.set_xlabel (label_x)
ax.set_ylabel (label_y)

# range
ax.set_xlim (per_min_day, per_max_day)

# plotting data
ax.plot (data_per_day, data_power, 'b-', \
         label='result of Lomb-Scargle periodogram')
ax.legend (bbox_to_anchor=(1.0, 1.12), loc='upper right')

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
