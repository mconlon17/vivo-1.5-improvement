"""
    test_improve_jobcode_description.py -- Given an HR abbreviation for a job title,
    resolve the various HR abbreviations to full text words.

    Version 0.1 MC 2013-12-27
    --  Initial version.
    Version 0.2 MC 2014-09-21
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.@"

from vivopeople import improve_jobcode_description
from datetime import datetime

print datetime.now(), "Start"
before = "SR TECH"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "ASS PROF"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "HLT MGR 3"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "GRD STUD"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "ADMIN AST"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "JR COMM SPC"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "VP"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "IT CLRK"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "BIO CHEM"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "AGRIC MSTR"
print "Before = ", before, "After = ", improve_jobcode_description(before)
before = "FIN ANAL"
print "Before = ", before, "After = ", improve_jobcode_description(before)
print datetime.now(), "Finish"

