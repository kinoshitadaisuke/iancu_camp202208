# importing math module
import math

# importing uncertainties module
import uncertainties
import uncertainties.umath

# quantity a
a = uncertainties.ufloat (20.0, 0.4)

# quantity b
b = uncertainties.ufloat (10.0, 0.3)

# calculation of c = a - b
c = a - b

# printing result of calculation
print ("a =", a)
print ("b =", b)
print ("c = a - b =", c)
