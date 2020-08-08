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


def getConfig(config_id,accountSwitchKey=None):
    """ Gets a specific policy on a given network in JSON format """

    print("Retrieving: " + config_id )
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        configdetail = prdHttpCaller.getResult("/client-access-control/v1/configurations/"
                                               + config_id,params)
    else:
        configdetail = prdHttpCaller.getResult("/client-access-control/v1/configurations/")

    return(configdetail)

def acknowledgeCidr(config_id,version_id,accountSwitchKey=None):
    """ Acknowledges CIDR for a specific version of CAC Config"""
    data = {}
    if accountSwitchKey:
        params = {'accountSwitchKey':accountSwitchKey}
        ackdetail = prdHttpCaller.putResult("/client-access-control/v1/configurations/"
                                               + config_id+"/acknowledge/"+version_id,data,params)
    else:
        ackdetail = prdHttpCaller.putResult("/client-access-control/v1/configurations/"
                                               + config_id+"/acknowledge/"+version_id,data)

    return(ackdetail)