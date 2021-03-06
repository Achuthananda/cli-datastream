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

from __future__ import print_function
import sys
import os
import logging
import random
import re
import requests
import json
import urllib
import texttable as tt
from future import standard_library
from future.builtins import next
from future.builtins import object
from http_calls import EdgeGridHttpCaller
from akamai.edgegrid import EdgeGridAuth,EdgeRc
from config import EdgeGridConfig
from subprocess import call
standard_library.install_aliases()
if sys.version_info[0] >= 3:
    # python3
    from urllib import parse
else:
    # python2.7
    import urlparse as parse

logger = logging.getLogger(__name__)

session = requests.Session()
debug = False
verbose = False
cache = False
format = "json"
section_name = "default"

# If all parameters are set already, use them.  Otherwise
# use the config
config = EdgeGridConfig({"verbose": False}, section_name)

if hasattr(config, "debug") and config.debug:
    debug = True

if hasattr(config, "verbose") and config.verbose:
    verbose = True

if hasattr(config, "cache") and config.cache:
    cache = True


# Set the config options
session.auth = EdgeGridAuth(
    client_token=config.client_token,
    client_secret=config.client_secret,
    access_token=config.access_token
)

if hasattr(config, 'headers'):
    session.headers.update(config.headers)

session.headers.update({'User-Agent': "AkamaiCLI"})

baseurl_prd = '%s://%s/' % ('https', config.host)
prdHttpCaller = EdgeGridHttpCaller(session, debug, verbose, baseurl_prd)


def listGroups(accountSwitchKey=None):
    """ List the groups associated with the account """

    listGroupEndpoint = '/datastream-config-api/v1/log/groups'
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        groupList = prdHttpCaller.getResult(listGroupEndpoint,params)
    else:
        groupList = prdHttpCaller.getResult(listGroupEndpoint)
    return(groupList)

def listConnectors(accountSwitchKey=None):
    """ List the type of connectors available with the datastream .
    Can use one of the connector types as a destination for log delivery in a data stream configuration"""

    listConnectorEndpoint = 'datastream-config-api/v1/log/connectors'

    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        connectorList = prdHttpCaller.getResult(listConnectorEndpoint,params)
    else:
        connectorList = prdHttpCaller.getResult(listConnectorEndpoint)
    return(connectorList)

def listProducts(accountSwitchKey=None):
    listProductEndpoint = 'datastream-config-api/v1/log/products'

    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        productsList = prdHttpCaller.getResult(listProductEndpoint,params)
    else:
        productsList = prdHttpCaller.getResult(listProductEndpoint)
    return(productsList)

def listStreamTypes(accountSwitchKey=None):
    """ List the type of streams available with the datastream."""

    listStreamTypeEndpoint = 'datastream-config-api/v1/log/streamTypes'

    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        streamTypeList = prdHttpCaller.getResult(listStreamTypeEndpoint,params)
    else:
        streamTypeList = prdHttpCaller.getResult(listStreamTypeEndpoint)
    return(streamTypeList)

def listStreams(groupId,status,accountSwitchKey=None):
    """ List the type of Streams available with the Group """

    listStreamsEndpoint = 'datastream-config-api/v1/log/streams'

    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey,
                  'groupId':str(groupId),
                  'streamStatus':status
                  }
        streamList = prdHttpCaller.getResult(listStreamsEndpoint,params)
    else:
        streamList = prdHttpCaller.getResult(listStreamsEndpoint)
    return(streamList)

def listProperties(groupId,productId,accountSwitchKey=None):
    """ List the type of Properties available with the Group """

    listPropertiesEndpoint = 'datastream-config-api/v1/log/properties/product/'+str(productId)+'/group/'+str(groupId)

    if accountSwitchKey:
        params = {
                    'accountSwitchKey':accountSwitchKey
                  }
        propertiesList = prdHttpCaller.getResult(listPropertiesEndpoint,params)
    else:
        propertiesList = prdHttpCaller.getResult(listPropertiesEndpoint)
    return(propertiesList)


def listErrorStreams(groupId,accountSwitchKey=None):
    """ List the type of Error Streams available with the Group """
    listErrorStreamsEndpoint = 'datastream-config-api/v1/log/error-streams/groups/' + str(groupId)
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        errorstreamList = prdHttpCaller.getResult(listErrorStreamsEndpoint,params)
    else:
        errorstreamList = prdHttpCaller.getResult(listErrorStreamsEndpoint)
    return(errorstreamList)

def getStream(streamId,accountSwitchKey=None):
    """Get the Details of the Stream """

    if hasattr(config, 'version') and config.version != 'latest':
        getStreamDetailEndpoint = '/datastream-config-api/v1/log/streams/' + str(streamId) + '/version/' + str(config.version)
    else:
        getStreamDetailEndpoint = '/datastream-config-api/v1/log/streams/' + str(streamId)

    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        streamDetail = prdHttpCaller.getResult(getStreamDetailEndpoint,params)
    else:
        streamDetail = prdHttpCaller.getResult(getStreamDetailEndpoint)
    return(streamDetail)

def getStreamActHistory(streamId,accountSwitchKey=None):

    streamActHistoryEndpoint = '/datastream-config-api/v1/log/streams/'+ str(streamId) + '/activationHistory'

    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        streamActHistory = prdHttpCaller.getResult(streamActHistoryEndpoint,params)
    else:
        streamActHistory = prdHttpCaller.getResult(streamActHistoryEndpoint)
    return(streamActHistory)


def getStreamHistory(streamId,accountSwitchKey=None):
    streamHistoryEndpoint = '/datastream-config-api/v1/log/streams/'+ str(streamId) + '/history'
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        streamHistory = prdHttpCaller.getResult(streamHistoryEndpoint,params)
    else:
        streamHistory = prdHttpCaller.getResult(streamHistoryEndpoint)
    return(streamHistory)

def getDatasets(templatename,accountSwitchKey=None):
    datasetsEndpoint = '/datastream-config-api/v1/log/datasets/template/'+ templatename
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        datasetList = prdHttpCaller.getResult(datasetsEndpoint,params)
    else:
        datasetList = prdHttpCaller.getResult(datasetsEndpoint)
    return(datasetList)


def createStream(data,accountSwitchKey=None):
    """ Create a Stream"""
    createEndpoint = '/datastream-config-api/v1/log/streams'
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        createResponse = prdHttpCaller.postResult(createEndpoint,data,params)
    else:
        createResponse = prdHttpCaller.postResult(createEndpoint,data)
    return(createResponse)

def updateStream(data,streamid,accountSwitchKey=None):
    """ Update a Stream"""
    updateEndpoint = '/datastream-config-api/v1/log/streams/' + str(streamid)
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        updateResponse = prdHttpCaller.putResult(updateEndpoint,data,params)
    else:
        updateResponse = prdHttpCaller.putResult(updateEndpoint,data)
    return(updateResponse)


def activateStream(streamId,accountSwitchKey=None):
    """ Activate a particular Datastream"""
    activateEndpoint = '/datastream-config-api/v1/log/streams/' + str(streamId) +'/activate/'
    data = {}
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        activateResponse = prdHttpCaller.putResult(activateEndpoint,data,params)
    else:
        activateResponse = prdHttpCaller.putResult(activateEndpoint,data)
    return(activateResponse)

def deActivateStream(streamId,accountSwitchKey=None):
    """ Deactivate a particular stream"""
    deactivateEndpoint = '/datastream-config-api/v1/log/streams/' + str(streamId) +'/deactivate/'
    data = {}
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        deactivateResponse = prdHttpCaller.putResult(deactivateEndpoint,data,params)
    else:
        deactivateResponse = prdHttpCaller.putResult(deactivateEndpoint,data)
    return(deactivateResponse)

def deleteStream(streamId,accountSwitchKey=None):
    """ Delete a particular stream"""
    deleteEndpoint = '/datastream-config-api/v1/log/streams/' + str(streamId)
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        deleteResponse = prdHttpCaller.deleteResult(deleteEndpoint,params)
    else:
        deleteResponse = prdHttpCaller.deleteResult(deleteEndpoint)
    return(deleteResponse)
