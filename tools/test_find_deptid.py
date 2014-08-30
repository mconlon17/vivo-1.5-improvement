"""
    test_find_deptid.py -- from a deptid dictionary, find deptids and return
    their URIs.

    Version 0.1 MC 2013-12-28
    --  Initial version.  Make a dictionary and make a dictionary with
        debug=True
    Version 0.2 MC 2014-08-30
    --  PEP 8, support vivofoundation
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivofoundation import make_deptid_dictionary
from vivofoundation import find_deptid
from datetime import datetime

print datetime.now(), "Start"
print datetime.now(), "Making deptid dictionary"
deptid_dictionary = make_deptid_dictionary(debug=True)
print datetime.now(), "deptid dictionary has ", len(deptid_dictionary), \
    "entries"
deptids = \
    [
        "02001000",
        "57000000",
        "29680000",
        "33100000",
        "16010000",
        "16020000",
        "60100000",
        "18300000",
        "27000000",
        "11040000"
    ]
for deptid in deptids:
    [found, uri] = find_deptid(deptid, deptid_dictionary)
    print str(found).ljust(5), deptid, uri

print datetime.now(), "Finished"
