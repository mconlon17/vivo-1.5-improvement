"""
    test_get_pubmed_values.py -- Given a doi, use Entrez to get the pubmed
    values from PubMed

    Version 0.1 MC 2013-12-28
    --  Initial version
    Version 0.2 MC 2014-09-18
    --  Upgraded for PEP 8 and Tools 2
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivopubs import get_pubmed_values
from datetime import datetime

print datetime.now(), "Start"
print "\n", get_pubmed_values("10.1111/j.1752-8062.2011.00348.x", debug=True)
print "\n", get_pubmed_values("10.1016/j.arcmed.2006.09.002")
print "\n", get_pubmed_values("unfindable")
print "\n", get_pubmed_values("10.1111/j.1365-2036.2010.04512.x")
print datetime.now(), "Finish"
