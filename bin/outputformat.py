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

def formatOutputStreamList(streamlist, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(streamlist, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([8,20,15,25,20,12])
        ParentTable.set_cols_align(['c','c','c','c','c','c'])
        ParentTable.set_cols_valign(['m','m','m','m','m','m'])
        Parentheader = ['StreamId','StreamName','CreatedBy','Properties','Connectors','Status']
        ParentTable.header(Parentheader)
        for my_item in streamlist:
            Parentrow = [ my_item["streamId"],my_item["streamName"],my_item["createdBy"],my_item["properties"],my_item["connectors"],my_item["activationStatus"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputStreamDetail(streamDetail, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(streamDetail, indent=2))

    if output_type == "text":
        print('Stream Id:',streamDetail['streamId'])
        print('Stream Name:',streamDetail['streamName'])
        print('Stream Version:',streamDetail['streamVersionId'])
        print('Stream Type:',streamDetail['streamType'])
        print('Connector Name:',streamDetail['connectors'][0]['connectorName'])
        print('Connector Type:',streamDetail['connectors'][0]['connectorTypeName'])
        print('Product Name:',streamDetail['productName'])
        print('Upload Frequency(in secs):',streamDetail['config']['frequency']['timeInSec'])
        print('Created By:',streamDetail['createdBy'])
        print('Datasets Selected:')

        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([25,10,25,35])
        ParentTable.set_cols_align(['c','c','c','c'])
        ParentTable.set_cols_valign(['m','m','m','m'])
        Parentheader = ['Group Name','Field Id','Field Name','Field Description']
        ParentTable.header(Parentheader)
        for my_item in streamDetail['datasetsInfos']:
            group_name = my_item["datasetGroupName"]
            for ds_item in my_item['dsFieldInfoList']:
                Parentrow = [group_name, ds_item["datasetFieldId"],ds_item["datasetFieldName"],ds_item["datasetFieldDesc"]]
                ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputActHistory(activationHistory, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(activationHistory, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([8,9,15,25,15])
        ParentTable.set_cols_align(['c','c','c','c','c'])
        ParentTable.set_cols_valign(['m','m','m','m','m'])
        Parentheader = ['StreamId','VersionId','CreatedBy','Created Date','Status']
        ParentTable.header(Parentheader)
        for my_item in activationHistory:
            status = "Inactive"
            if my_item["isActive"] == True:
                status = "Active"
            Parentrow = [ my_item["streamId"],my_item["streamVersionId"],my_item["createdBy"],my_item["createdDate"],status]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)
