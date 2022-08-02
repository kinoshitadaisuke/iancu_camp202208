# importing math module
import math

# catalogue file
file_catalogue = 'bsc5.data'

# an empty list to store B-V colour index
list_bv = []

# opening file
with open (file_catalogue, 'r') as fh:
    # reading file
    for line in fh:
        # ID number of star
        hr_number = int (line[0:4])
        # B-V colour index of star
        try:
            bv_colour = float (line[109:114])
        except:
            bv_colour = math.nan
        # spectral type of star
        sptype = line[127:147].strip ()
        # if star is not G2V star, then skip
        if not (sptype == 'G2V'):
            continue
        # if B-V colour index is not nan (not a number),
        # then add B-V colour index to the list
        if not ( math.isnan (bv_colour) ):
            list_bv.append (bv_colour)

# calculation of mean and standard deviation
n = len (list_bv) # number of data
bv_sum    = 0.0   # initialisation of "bv_sum"
bv_sum_sq = 0.0   # initialisation of "bv_sum_sq"
for bv in list_bv:
    # adding B-V colour index of a star to "bv_sum"
    bv_sum    += bv
    # adding square of B-V colour index of a star to "bv_sum_sq"
    bv_sum_sq += bv**2
# calculation of mean
bv_mean   = bv_sum / n
# calculation of standard deviation
bv_stddev = math.sqrt ( bv_sum_sq / n - bv_mean**2 )

# printing result
print ("mean colour of G2V stars = %+5.2f +/- %4.2f" \
       % (bv_mean, bv_stddev) )
