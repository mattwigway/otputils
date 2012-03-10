#!/usr/bin/python

# Copyright (C) 2012 Matt Conway.

# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from optmatch import OptionMatcher, optmatcher
import csv
import json
import re
from sys import argv

class ParseGraphBuilderLogToGeoJSON(OptionMatcher):
    @optmatcher
    def handle(self, logfile, stopsfile, jsonfile, agency=None):
        self.logfile = open(logfile, 'r')
        self.stopsfile = open(stopsfile, 'r')
        self.outfile = open(jsonfile, 'w')

        if not agency:
            agency = r'.*'
            

        print r'WARN  [NetworkLinker.java:66] : Stop <' + agency + r'_.*> not near any streets; it will not be usable'
        self.stopUnlinkedRe = re.compile(r'WARN  \[NetworkLinker.java:66\] : Stop <' + agency + r'_.*> not near any streets; it will not be usable')

        # Init a GeoJSON container
        self.output = []

        self.loadStops()
        self.parseLog()
        self.writeOutfile()

    def loadStops(self):
        """Parse the files and prepare self.stops"""

        # Parse the stops
        print 'Loading stops into RAM'
        self.stops = {}
        reader = csv.reader(self.stopsfile)
        # Save the column headings
        firstRow = reader.next()
        for line in reader:
            # Attach column names and convert todict
            stop = dict(zip(firstRow, line))
            self.stops[stop['stop_id']] = stop
        print 'Loaded %s stops' % len(self.stops)

    def parseLog(self):
        self.output = dict(
            type='FeatureCollection',
            features = []
            )
        matchedLines = [line for line in self.logfile if self.isUnlinked(line)]
        print 'matched %s lines' % len(matchedLines)
        for line in matchedLines:
            stop = self.stops[self.getId(line)]
            self.output['features'].append(self.makeGeoJSON(stop))

    def isUnlinked(self, line):
        if (self.stopUnlinkedRe.search(line) != None):
            return True
        else:
            return False

    def getId(self, line):
        # This is sadly hacky
        return line.split('_')[1].split('>')[0]

    # turn a stop into a GeoJSON object
    def makeGeoJSON(self, stop):
        return dict(
            type = 'Feature',
            id = stop['stop_id'],
            properties = stop,
            geometry = dict(
                type = 'Point',
                coordinates = [float(stop['stop_lon']), float(stop['stop_lat'])]
                ),
            crs = dict(
                type = 'name',
                properties = dict(
                    #WGS 84
                    name = 'urn:ogc:def:crs:OGC:1.3:CRS84'
                    )
                )
            )
    
    def writeOutfile(self):
        json.dump(self.output, self.outfile)

ParseGraphBuilderLogToGeoJSON().process(argv)
