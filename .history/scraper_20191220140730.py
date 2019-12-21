#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.

There should be a blank line in between description above, and this
more detailed description. In this section you should put any caveats, 
environment variable expectations, gotchas, and other notes about running
the program.  Author tag (below) helps instructors keep track of who 
wrote what, when grading.
"""
__author__ = "Enrique Galindo"

# Imports go at the top of your file, after the module docstring.
# One module per import line. These are for example only.
import sys



# This statement will run once at module import.
print("Executing module import, name is {}".format(__name__))

# declare a few constants
MY_MODULE_PI = pi





if __name__ == '__main__':
    """Docstring goes here"""
    print("Command line arguments: {}".format(sys.argv))
    # Invoke standalone main() with cmdline argument list.
    # Program should return status==0 if no errors.
    status = main(sys.argv)
    # return status code to OS.
    sys.exit(status)