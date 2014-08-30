"""
    demo_sample_uf_faculty.py -- Generate a random sample of current UF faculty

    Version 0.1 MC 2013-12-27
    --  Initial version
    Version 0.2 MC 2014-08-30
    --  Updated for vivofoundation, code formatting for PEP 8
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivofoundation import vivo_sparql_query
import random
from datetime import datetime

query = """
    SELECT ?uri WHERE
    {
    ?uri a vivo:FacultyMember .
    ?uri a ufVivo:UFCurrentEntity .
    }
"""
print datetime.now(), "Gathering Current UF Faculty from VIVO"
data = vivo_sparql_query(query)
print datetime.now(), "Current UF Faculty found = ", \
    len(data["results"]["bindings"])
print datetime.now(), "Load data structure with results"
d = []
for item in data["results"]["bindings"]:
    d.append(item["uri"]["value"])
print datetime.now(), "Select random sample"
random.shuffle(d)
print datetime.now(), "Show selected faculty by VIVO URI"
for i in range(100):
    print d[i]
print datetime.now(), "Finished"

