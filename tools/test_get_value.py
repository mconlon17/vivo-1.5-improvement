"""
    test_get_value.py -- Given a subject URi and a predicate,
    get the value of the object.  Returns a dict

    Version 0.1 MC 2014-03-27
    --  Initial version.

"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.1"

from vivofoundation import get_value
from datetime import datetime

print datetime.now(), "Start"

print get_value("http://vivo.ufl.edu/individual/n25562", "foaf:lastName")
print get_value("http://vivo.ufl.edu/individual/n1278130", "rdfs:label")
print get_value("http://vivo.ufl.edu/individual/n42412", "rdfs:label")
print get_value("http://vivo.ufl.edu/individual/n25562", "foaf:noName")
print get_value("http://vivoweb.org/ontology/degree/academicDegree4",
                "core:abbreviation")

print datetime.now(), "Finish"
