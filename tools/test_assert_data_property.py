"""
    test_assert_data_property.py -- Given a URI, a vivo data property predicate
    and a value, generate RDF for asserting thar the URI has the data property
    value.  The tests demonstrate that that the function does not check for
    a valid predicate, nor a valid value.

    The value can be a string or a dictionary.  If a dictionary, the elements
    should be 'value', 'xml:lang', and/or 'datatype'.  'value' is required.

    Version 0.1 MC 2013-12-27
    --  Initial version
    Version 0.2 MC 2014-03-27
    --  Demonstrate value as string or dictionary, lang and datatype support
    Version 0.3 MC 2014-08-30
    --  PEP 8 improvements, support vivofoundation
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.3"

from vivofoundation import assert_data_property
from datetime import datetime

print datetime.now(), "Start"

print assert_data_property("http://a.b", "rdfs:label", "Blue Moon")
print assert_data_property("http://a.b", "vivo:phoneNumber", "5")
print assert_data_property("http://a.b", "vivo:phoneNumber", {'value': '6',
    'xml:lang':'en-US'})
print assert_data_property("http://a.b", "vivo:phoneNumber", {'value': '7'})
print assert_data_property("http://a.b", "vivo:phoneNumber", {'value': '6',
    'datatype':'http://www.w3.org/2001/XMLSchema#string'})
print assert_data_property("http://a.b", "vivo:phoneNumber", {'value': '6',
    'xml:lang':'en-US', 'datatype': 'http://www.w3.org/2001/XMLSchema#string'})
print assert_data_property("http://a.b", "bibo:abstract",
    "We escape nasty ampersands & other characters that <trip up> RDF")

print datetime.now(), "Finish"

