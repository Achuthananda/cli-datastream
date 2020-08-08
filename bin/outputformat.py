# Python edgegrid module
""" Copyright 2015 Akamai Technologies, Inc. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.

 You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import sys
import os
import requests
import logging
import json
import texttable as tt

from akamai.edgegrid import EdgeGridAuth, EdgeRc
from config import EdgeGridConfig
if sys.version_info[0] >= 3:
    # python3
    from urllib import parse
else:
    # python2.7
    import urlparse as parse

logger = logging.getLogger(__name__)



def formatOutputGroupList(grouplist, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(grouplist, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([25,30])
        ParentTable.set_cols_align(['c','c'])
        ParentTable.set_cols_valign(['m','m'])
        Parentheader = ['Group Id','Group Name']
        ParentTable.header(Parentheader)
        for my_item in grouplist:
            Parentrow = [ my_item["groupId"],my_item["groupName"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputConnectorList(connectorlist, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(connectorlist, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([25,30])
        ParentTable.set_cols_align(['c','c'])
        ParentTable.set_cols_valign(['m','m'])
        Parentheader = ['ConnectorType Id','ConnectorType Name']
        ParentTable.header(Parentheader)
        for my_item in connectorlist:
            Parentrow = [ my_item["connectorTypeId"],my_item["connectorTypeName"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)
