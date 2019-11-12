""" __doc__ """

import functions

# import csv and populate a dictionary with its contents
functions.populate_dct()

# print number of occurances
print functions.RTN()
for k, v in sorted(functions.DESCRIPTIONS_DCT.iteritems(), \
key=lambda x: x[1][2]):
    if v[2] > 1:
        print(f"number: %s {k}")
        print(f"client: %s {v[0]}")
        print(f"short description: {v[1]}")
        print(f"number of requests: {v[2]}")
        print(functions.RTN())
    else:
        pass
