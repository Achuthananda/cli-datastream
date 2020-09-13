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


def formatOutputProductList(productsList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(productsList, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([20,25,25,15])
        ParentTable.set_cols_align(['c','c','c','c'])
        ParentTable.set_cols_valign(['m','m','m','m'])
        Parentheader = ['Product','Product Id','Groups','Templates']
        ParentTable.header(Parentheader)

        for my_item in productsList:
            group_ids = []
            template_list = []
            for group in my_item["groups"]:
                group_ids.append(group["groupId"])
                for child_ids in group["childGroups"]:
                    group_ids.append(child_ids["groupId"])

            for template_item in my_item["templates"]:
                template_list.append(template_item["templateName"])

            Parentrow = [ my_item["productName"],my_item["productId"],group_ids,template_list]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputStreamTypeList(streamTypeList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(streamTypeList, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([14,10,8])
        ParentTable.set_cols_align(['c','c','c'])
        ParentTable.set_cols_valign(['m','m','m'])
        Parentheader = ['StreamTypeName','StreamType','Raw']
        ParentTable.header(Parentheader)
        for my_item in streamTypeList:
            raw = "No"
            if my_item["isRaw"] == True:
                raw = "Yes"
            Parentrow = [my_item["streamTypeName"],my_item["streamType"],raw]
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

def formatOutputPropertiesList(propertieslist, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(propertieslist, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([8,30])
        ParentTable.set_cols_align(['c','c'])
        ParentTable.set_cols_valign(['m','m'])
        Parentheader = ['PropertyId','PropertyName']
        ParentTable.header(Parentheader)
        for my_item in propertieslist:
            Parentrow = [ my_item["propertyId"],my_item["propertyName"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputErrorStreamList(streamlist, output_type):
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
        print('Connector Type:',streamDetail['connectors'][0]['connectorType'])
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
        for my_item in streamDetail['datasets']:
            group_name = my_item["datasetGroupName"]
            for ds_item in my_item['datasetFields']:
                Parentrow = [group_name, ds_item["datasetFieldId"],ds_item["datasetFieldName"],ds_item["datasetFieldDescription"]]
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

def formatOutputStreamHistory(streamHistory, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(streamHistory, indent=2))

    if output_type == "text":
        for my_item in streamHistory:
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Stream ID:",my_item['streamId'])
            print("Stream Version:",my_item['streamVersionId'])
            print("Stream Name:",my_item['streamName'])
            print("Product Name",my_item['productName'])
            print("DataSets:")
            for dataset_info in my_item["datasets"]:
                    dataset_name = dataset_info["datasetGroupName"]
                    field_list = []
                    for fields in dataset_info["datasetFields"]:
                        field_list.append(fields['datasetFieldName'])
                    print(dataset_name,":",field_list)

        print("------------------------------------------------------------------------------------------------------------------------------------------------------")

def formatOutputDatasetList(datasetList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(datasetList, indent=2))

    if output_type == "text":
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([25,10,25,35])
        ParentTable.set_cols_align(['c','c','c','c'])
        ParentTable.set_cols_valign(['m','m','m','m'])
        Parentheader = ['Group Name','Field Id','Field Name','Field Description']
        ParentTable.header(Parentheader)
        for my_item in datasetList:
            group_name = my_item["datasetGroupName"]
            for ds_item in my_item['datasetFields']:
                Parentrow = [group_name, ds_item["datasetFieldId"],ds_item["datasetFieldName"],ds_item["datasetFieldDescription"]]
                ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputActDeactResp(actdeactivateResponse):
    print(json.dumps(actdeactivateResponse, indent=2))
