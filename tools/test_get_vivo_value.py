"""
    test_get_vivo_value.py -- Given a subject URi and a predicate,
    get the value of the object.  Assumes the object is single valued.

    Version 0.1 MC 2013-12-30
    --  Initial version.
    Version 0.2 MC 2014-09-02
    --  PEP 8, vivofoundation

"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivofoundation import get_vivo_value
from datetime import datetime

print datetime.now(), "Start"

print get_vivo_value("http://vivo.ufl.edu/individual/n25562", "foaf:lastName")
print get_vivo_value("http://vivo.ufl.edu/individual/n1278130",
                     "rdfs:label")
print get_vivo_value("http://vivo.ufl.edu/individual/n25562", "foaf:noName")
print get_vivo_value("http://vivoweb.org/ontology/degree/academicDegree4",
                     "vivo:abbreviation")

print datetime.now(), "Finish"
