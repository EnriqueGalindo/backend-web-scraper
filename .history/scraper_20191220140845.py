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


def main(args):
    """Main function is declared as standalone, for testability"""
    # You can call this main() function even if it is imported by
    # another program.
    print("main args: {}".format(args))
    # get the first argument, do something cool
    my_arg0 = args[0]
    result = first_helper_func(my_arg0)
    # return 0 if everything is awesome, nonzero otherwise ...
    print('result is {}'.format(result))
    return 0


if __name__ == '__main__':
    """Docstring goes here"""
    main(sys.argv[1:])