""" __doc__ """

import functions

# import csv and populate a dictionary with its contents
functions.populate_dct()

# company field is empty
print functions.RTN()
print "company is empty".upper()
for k, v in functions.DESCRIPTIONS_DCT.items():
    if not v[0]:
        print k, v[1]
