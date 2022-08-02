# name of data file
file_data = 'drink.data'

# initialisation of variable 'total_price'
total_price = 0

# opening file using reading mode
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # skipping line if starting with '#'
        if (line[0] == '#'):
            continue
        # splitting the line into multiple fields
        (name, unit_price, quantity) = line.split ()
        # converting string into integer
        unit_price = int (unit_price)
        quantity   = int (quantity)
        # calculation of sub-total
        subtotal = unit_price * quantity
        # calculation of total price
        total_price += subtotal
        # printing information
        print ("%-10s  %3d  %2d  %3d" \
               % (name, unit_price, quantity, subtotal) )

# printing total price
print ("==========")
print ("total price: %d" % (total_price) )
