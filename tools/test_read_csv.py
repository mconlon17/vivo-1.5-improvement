"""
    test_read_csv.py -- given a CSV file, read it into a python dictionary

    Version 0.1 MC 2013-12-27
    --  Initial version
    Version 0.2 MC 2014-08-30
    --  PEP 8, vivofoundation
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2013, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivofoundation import read_csv
from datetime import datetime

print datetime.now(), "Start"

data = read_csv("data_test_read_csv.csv")
print "Data file has", len(data.keys()), "rows and", len(data[1]),"columns"
print "The data as one structure:", data
print "Display the data as rows and columns:"

names = data[1].keys()
for name in names:
    print name,
print

for row in sorted(data.keys()):
    line = data[row]
    for val in line.values():
        print val,
    print


print datetime.now(), "Finish"
