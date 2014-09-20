"""
    test_get_publication.py -- Given a URI of an publication, return a python
    structure representing the attributes of the publication

    Version 0.1 MC 2013-12-27
    --  Initial version.
    Version 0.2 MC 2014-09-18
    --  Update for PEP 8, and tools 2.0

"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivopubs import get_publication
from vivopubs import string_from_document
from datetime import datetime

print datetime.now(), "Start"
publications = \
    [
        "http://vivo.ufl.edu/individual/n2592711416",
        "http://vivo.ufl.edu/individual/n49408",
        "http://vivo.ufl.edu/individual/n5988333327",
        "http://vivo.ufl.edu/individual/n697590874",
        "http://vivo.ufl.edu/individual/n7170943995",
        "http://vivo.ufl.edu/individual/no-such-pub",
        "http://vivo.ufl.edu/individual/n536643140",
        "http://vivo.ufl.edu/individual/n5202165124",
        "http://vivo.ufl.edu/individual/n898775618",
        "http://vivo.ufl.edu/individual/n5755807043"
    ]
for publication in publications:
    pub = get_publication(publication, get_authors=True)
    print "\n", pub
    print string_from_document(pub)
print datetime.now(), "Finish"
