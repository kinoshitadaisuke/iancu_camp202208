# importing math module
import math

# brightness ratio of RR Lyrae at its maximum and minimum
F_ratio = 2.0

# calculation of magnitude change of RR Lyrae
# using Pogson's formula
# m1 - m2 = -2.5 log10 (F1/F2)
Delta_mag = abs ( -2.5 * math.log10 (F_ratio) )

# printing result of calculation
print ("mag change of RR Lyrae = %4.2f mag" % (Delta_mag) )
