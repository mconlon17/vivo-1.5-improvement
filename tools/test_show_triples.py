"""
    test_show_triples.py -- print a tabular result from the returns of get_triples

    Version 0.1 MC 2013-12-27
    --  Initial version
    Version 0.2 MC 2014-09-02
    --  PEP 8, vivofoundation
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD-3"

from vivofoundation import show_triples
from vivofoundation import get_triples
from datetime import datetime

#  Test cases for access and display functions

print datetime.now, "Start"

print "\nDateTime"
print show_triples(get_triples("http://vivo.ufl.edu/individual/n7860108656"))


print "\nDateTimeInterval"
print show_triples(get_triples("http://vivo.ufl.edu/individual/n182882417"))

print "\nOrganization"
print show_triples(get_triples("http://vivo.ufl.edu/individual/n8763427"))


print "\nAuthorship"
print show_triples(get_triples("http://vivo.ufl.edu/individual/n148010391"))

print "\nRole"
print show_triples(get_triples("http://vivo.ufl.edu/individual/n1864549239"))


print "\nPerson"
print show_triples(get_triples("http://vivo.ufl.edu/individual/n39051"))

print "\nNot Found"
print show_triples(get_triples("http://vivo.ufl.edu/notfound"))

print "\nPublication Venue"
print show_triples(get_triples("http://vivo.ufl.edu/individual/n378789540"))

print "\nPaper"
print show_triples(get_triples("http://vivo.ufl.edu/individual/n4703866415"))

print "\nGrant"
print show_triples(get_triples("http://vivo.ufl.edu/individual/n614029206"))

print datetime.now(), "End"

