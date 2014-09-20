"""
    test_get_references.py -- Given a URI, get the references for the URI

    Version 0.1 MC 2013-12-27
    --  Initial version.
    Version 0.2 MC 2014-09-18
    --  Update for PEP 8 and Tools 2
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivofoundation import get_references
from datetime import datetime

#  Test cases for access and display functions

print datetime.now(), "Start"

print "\nDateTime"
print get_references("http://vivo.ufl.edu/individual/n7860108656")


print "\nDateTimeInterval"
print get_references("http://vivo.ufl.edu/individual/n182882417")

print "\nOrganization"
print get_references("http://vivo.ufl.edu/individual/n8763427")

print "\nAuthorship"
print get_references("http://vivo.ufl.edu/individual/n148010391")

print "\nRole"
print get_references("http://vivo.ufl.edu/individual/n1864549239")

print "\nPerson"
print get_references("http://vivo.ufl.edu/individual/n39051")

print "\nNot Found"
print get_references("http://vivo.ufl.edu/notfound")

print "\nPublication Venue"
print get_references("http://vivo.ufl.edu/individual/n378789540")

print "\nPaper"
print get_references("http://vivo.ufl.edu/individual/n4703866415")

print "\nGrant"
print get_references("http://vivo.ufl.edu/individual/n614029206")

print datetime.now(), "Finish"

