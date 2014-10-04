#!/usr/bin/python

## @scanner.py
#  This script takes a single argument, a file which is passed as an argument
#      to the imported 'data_validator.py', which validates for proper syntax.
#
#      Once syntax has been validated, 'data_validator' will return 'true'.
#      This will allow the imported 'data_calculator.py', to return an object
#      containing necessary calculation results.  The returned calculation
#      results will then be written to 'log/observation.log'
#
#  Terminology:
#      - Slew time: time spent moving the dish
#      - Time on source: applies to 'variable scans' and defined as:
#
#            time on source (mins) = -2 x (flux density) + 20.5
#
#      - Total time: the sum of the two.

## import
#    Validator: class used to validate input data
#    sys.path : search path for modules
import sys
sys.path.append('log/')
sys.path.append('lib/')
from data_validator import Validator
from data_calculator import Observation

# instatiate validator
if len(sys.argv) > 1:
  validator = Validator(sys.argv[1])

# check input file format, and perform calculation
if len(sys.argv) > 1 and validator.is_file():
  if validator.check_format():
    observation = Observation(sys.argv[1])
    observation.calculation()
    observation_result = observation.get_result()

    # create 'log/' directory if doesn't exist
    os.makedirs('/foo/bar', exist_ok=True)

    # save 'observation_result' to 'observation.log'
    with open('log/observation.log', 'w') as f:
      for line in observation_result:
        f.write(line + '\n')
else:
  print 'Please include a proper text file (.txt)'
