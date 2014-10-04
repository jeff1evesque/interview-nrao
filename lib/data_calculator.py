#!/usr/bin/python

## data_calculator.py
from data_validator import Validator

## Class: Observation
class Observation:

    ## Constructor:
    #  @line.strip(): removes '\n' from the 'line'
    #  @filter(None, sequence): filter out elements evaluating to False
    def __init__(self, file):
        # create 'log/' directory if doesn't exist

        # store input file
        self.file = file

        # store input file into sublists.
        self.data_list = []
        with open(self.file) as f:
          input_data = filter(None, [ line.strip() for line in f ])
          for idx, line in enumerate(input_data):
            self.data_list.append(line.split())

        # initial input data
        self.scan_type            = self.data_list[0][0]

        self.azimuth_change       = self.data_list[0][1]
        self.elevation_change     = self.data_list[0][2]
        self.flux_density_change  = self.data_list[0][3]

        self.total_slew_time      = 0
        self.total_time_on_source = 0
        self.total_time           = 0

        # scan computation result
        self.scan_result = []

    ## calculation():
    def calculation(self):      

      for idx, item in enumerate(self.data_list):
        # update values on next scan
        if idx > 0:
          self.scan_type            = self.data_list[idx][0]

          self.azimuth_change       = format( abs(float(self.data_list[idx][1]) - float(self.data_list[idx - 1][1])), '.3f' )
          self.elevation_change     = format( abs(float(self.data_list[idx][2]) - float(self.data_list[idx - 1][2])), '.3f' )
          self.flux_density_change  = format( abs(float(self.data_list[idx][3])), '.3f' )

        # calculation: time on source
        if self.scan_type.lower() == 'c':
          time_on_source = format( float(2), '.3f')
        elif self.scan_type.lower() == 't':
          time_on_source = format( float(5), '.3f')
        elif self.scan_type.lower() == 'v':
          time_on_source = format( (float(-2) * float(self.flux_density_change)) + float(20.5), '.3f' )
        self.total_time_on_source = format( float(self.total_time_on_source) + float(time_on_source), '.3f' )

        # calculation: slew time
        slew_time_azimuth   = format(float(self.azimuth_change) / 40 , '.3f')
        slew_time_elevation = format(float(self.elevation_change) / 20, '.3f')

        if slew_time_azimuth > slew_time_elevation:
          slew_time = slew_time_azimuth
        else:
          slew_time = slew_time_elevation
        self.total_slew_time = format(float(self.total_slew_time) + float(slew_time), '.3f')

        # calculation: total time
        total_time = format(float(time_on_source) + float(slew_time), '.3f')
        self.total_time = format(float(self.total_time) + float(total_time), '.3f')

        # append result values to 'self.scan_result'
        self.scan_result.append( '#' + str(idx+1) + ': ' + str(self.scan_type) + ' ' + str(total_time) + ' ' + str(slew_time) + ' ' + str(time_on_source) )

    ## get_result():
    def get_result(self):
      total_observation = self.total_time + ' ' + self.total_slew_time + ' ' + self.total_time_on_source
      self.scan_result.append( total_observation )

      return self.scan_result
