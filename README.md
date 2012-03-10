This is a collection of tools that do things with
[OpenTripPlanner](http://opentripplanner.org). So far, they are all
written by Matt Conway, but if you'd like to add some, please send
pull requests. Language/platform no barrier. Any additions should be
LGPL-licensed.

Tools available now:

* parseGraphBuilderLogToGeoJSON: parses out unlinked stops from a
  graph builder log and creates a GeoJSON file. Specify the log file,
  the path to stops.txt for one of your GTFS files, the GeoJSON output
  file and, if you're using a multiagency graph, the agency to
  parse. If you want to use it for more than one agency, run it
  multiple times (feel free to fix that).
  
 
This repository includes code (optmatch.py, which is awesome by the
way) that is:
Copyright (c) Luis M. Pena <lu@coderazzi.net>  All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
Redistributions in bytecode form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in
the documentation and/or other materials provided with the
distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
