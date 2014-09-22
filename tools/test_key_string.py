"""
    test_key_string.py -- from text, make a key string for use in dictionaries
    where text may not match exactly, such as publication and grant titles

    Version 0.1 MC 2013-12-27
    --  Initial version
    Version 0.2 MC 2014-09-21
    --  PEP 8, Tools 2
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivofoundation import key_string
from datetime import datetime

#  Test cases


print datetime.now(), "Start"
print key_string("  A +Walk+ in (the) Woods")
print key_string("A wALK  in the, woods   ")
print key_string("AWALKINTHEWOODS")
print key_string("awalkinthewoods")
print datetime.now(), "Finish"
