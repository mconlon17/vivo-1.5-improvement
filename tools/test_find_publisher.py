"""
    test_find_publisher.py -- from a publisher dictionary, find publishers and
    return their URIs.

    Version 0.1 MC 2013-12-28
    --  Initial version.  Make a dictionary and make a dictionary with
        debug=True
    Version 0.2 MC 2014-08-30
    --  PEP 8, support for vivopubs
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivopubs import make_publisher_dictionary
from vivopubs import find_publisher
from datetime import datetime

print datetime.now(), "Start"
print datetime.now(), "Making publisher dictionary"
publisher_dictionary = make_publisher_dictionary(debug=True)
print datetime.now(), "publisher dictionary has ", len(publisher_dictionary),\
    "entries"
publishers = \
    [
        "The Society of Photo-Optical Instrumentation Engineers",
        "The Times-Picayune News",
        "The Unfindable Publisher",
        "Thieme Medical Publishers Inc",
        "Thomas Land Publishers, Inc",
        "Thomson Reuters (Scientific) Ltd",
        "Thomson Scientific",
        "Thorne Research, Inc",
        "Times Supplements Limited",
        "Tohoku University Medical Press",
        "Torrey Botanical Society"
    ]
for publisher in publishers:
    [found, uri] = find_publisher(publisher, publisher_dictionary)
    print str(found).ljust(5), publisher, uri

print datetime.now(), "Finished"
