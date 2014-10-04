#!/usr/bin/python

## @data_validator.py
#  This script validates whether a given parameter is a valid file, and
#      whether the given file contains data that is correctly formatted.
import sys, os

## Class: Validator
class Validator:

    ## Constructor: intializes the input data file to a class property.
    def __init__(self, file = None):
        self.file = file

    ## is_file: determines if 'self.file' is file, and has 'txt' extension
    def is_file(self):
        file_path = os.path.abspath(self.file)
        if os.path.isfile(file_path) and self.file.endswith('.txt'):
            return True
        else:
            return False

    ## check_format: checks each row (scan) within the input file. Each row
    #                must be of the form:
    #
    #      <a> <bbb.bb>  <cc.cc> <dd.dd>
    #
    #          a: denotes the 'scan type'.  It can only be one of the following
    #              string options:
    #                  'C' - Calibration scan
    #                  'T' - Target scan
    #                  'V' - Variable scan
    #
    #          b: denotes the 'azimuth' value.  It can only contain floating
    #              point numbers from 0.00 to 360.00
    #
    #          c: denotes the 'elevation' value.  It can only contain floating
    #              numbers from 0.00 to 90.00
    #
    #          d: denotes the 'flux density' value.  It can only contain floating
    #              point numbers from 0.5 to 10.0
    #
    #      In order to make the above validation, we use 'check_type()' to check
    #          the values for <bbb.bb>, <cc.cc>, and <dd.dd>
    def check_format(self):
        scan_type = ['c', 't', 'v']
        with open(self.file) as f:
            content = filter(None, [ line.strip() for line in f ])
            for idx, line in enumerate(content):
                scan_list = line.split()
                if scan_list[0].lower() not in str(scan_type):
                    print 'Error: ' + self.file + ', line ' + str(idx + 1) + ', column 1 has incorrect format.'
                    print '       ' + col_scanType + " must have the form 'C', 'T', or 'V'\n"
                    sys.exit()
                self.check_type(scan_list[1], idx, 2, 'float', 0, 360)
                self.check_type(scan_list[2], idx, 3, 'float', 0, 90)
                self.check_type(scan_list[3], idx, 4, 'float', 0.5, 10)
                return True

    ## check_type(): is called from 'check_format', and ensures that 'val' is of
    #                type 'value_type'.  And checks that 'val' is between the
    #                given bound 'low_bound', and 'hi_bound'.
    #
    #  @val: the value to check.
    #  @row: the scan, or row within the input data
    #  @col: the column data within a scan of an input data
    #  @value_type: the value to check against. Specifically, we try to convert it
    #               to this value.  Otherwise, we print an error, and exit
    #  @low_bound: the allowed lower bound for the value 'val'
    #  @hi_bound:  the allowed uppper bound for the value 'val'.
    def check_type(self, val, row, col, value_type, low_bound, hi_bound):
        try:
          exec 'val = ' + value_type + '(' + val + ')'
        except:
            print 'Error: ' + self.file + ', line ' + str(row + 1) + ', column ' + str(col) + ' has incorrect format.'
            print '       The column data ' + str(val) + ' must be of type ' + value_type + '\n'
            sys.exit()
        if val < low_bound or val > hi_bound:
            print 'Error: ' + self.file + ', line ' + str(row + 1) + ', column ' + str(col) + ' has incorrect format.'
            print '       The column data ' + str(val) + ' must be contained between the bounds [' + str(low_bound) + ', ' + str(hi_bound) + ']\n'
            sys.exit()
