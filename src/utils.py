# Data
# This handles storing data. This abstracts the process so it can be dia via DB or a JSON file 
####################################################################################################
import json
import os, sys, time


class Data:


    def __init__(self, output_file, init_schema):
        self.output = output_file
        self.data = {}

        # Create file if it does not exist
        if not os.path.exists(self.output):
            with open(self.output, 'w') as file:
                json.dump(init_schema, file)
        # If file is empty
        if os.stat(self.output).st_size == 0:
            with open(self.output, 'w') as file:
                json.dump(init_schema, file)


    @staticmethod
    def _write_file(target, data):
        # Wait for data lock to finish
        lock_suffix = '.lock'
        while(os.path.exists(target + lock_suffix)):
            # Sleep to avoid writing to a file that is locked
            time.sleep(1.0)
        # Create data lock
        with open(target + lock_suffix, 'w') as lock_file:
            json.dump({'file':'is_locked'}, lock_file)

        # Write data
        with open(target, 'w') as output_file:
            json.dump(data, output_file)

        # Remove data lock
        os.remove(target + lock_suffix)


    def write(self, data):
        Data._write_file(self.output, data)


    @staticmethod
    def _read_file(target):
        with open(target, 'r') as input_file:
            return json.load(input_file)


    def read(self):
        return Data._read_file(self.output)

########################################################################################################
#   Copyright (C) 2022  Rhydian Davies, Liam Coombs
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
