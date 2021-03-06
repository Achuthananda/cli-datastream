# Python edgegrid module - CONFIG for ImgMan CLI module
""" Copyright 2017 Akamai Technologies, Inc. All Rights Reserved.

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
import argparse
import logging

if sys.version_info[0] >= 3:
    # python3
    from configparser import ConfigParser
    import http.client as http_client
else:
    # python2.7
    from ConfigParser import ConfigParser
    import httplib as http_client

PACKAGE_VERSION = "0.1.8"

logger = logging.getLogger(__name__)

class EdgeGridConfig():

    parser = argparse.ArgumentParser(description='Process command line options.')

    def __init__(self, config_values, configuration, flags=None):
        parser = self.parser
        parser.add_argument('--verbose', '-v',default=False, action='count', help=' Verbose mode')
        parser.add_argument('--debug', '-d', default=False, action='count', help=' Debug mode (prints HTTP headers)')
        parser.add_argument('--edgerc', '-e', default='~/.edgerc', metavar='credentials_file', help=' Location of the credentials file (default is ~/.edgerc)')
        parser.add_argument('--section', '-c', default='ds', metavar='credentials_file_section', action='store', help=' Credentials file Section\'s name to use')
        parser.add_argument('--accountSwitchKey', '-a', metavar='Account Switch Key', action='store', help=' Switch key to different account')


        subparsers = parser.add_subparsers(help='commands', dest="command")

        list_group_parser = subparsers.add_parser("list-groups", help="List all Groups in the Account")
        list_group_parser.add_argument('--output-type', '-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type {json, text}. Default is text')

        list_connectors_parser = subparsers.add_parser("list-connectors", help="List all Connectors.")
        list_connectors_parser.add_argument('--output-type', '-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type {json, text}. Default is text')

        list_stream_type_parser = subparsers.add_parser("list-stream-types", help="List all Types of Stream.")
        list_stream_type_parser.add_argument('--output-type', '-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type {json, text}. Default is text')

        list_streams_parser = subparsers.add_parser("list-streams", help="List all Streams.")
        list_streams_parser.add_argument('groupid', help="Group id for which streams need to be retrieve", action='store')
        list_streams_parser.add_argument('--streamstatus','-s', default='ACTIVATED', choices=['ACTIVATED', 'DEACTIVATED','IN_PROGRESS'],metavar='activated/deactivated/in_progress', help=' Status of the stream. Default is Activated')
        list_streams_parser.add_argument('--output-type', '-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type {json, text}. Default is text')


        list_properties_parser = subparsers.add_parser("list-properties", help="List all Properties.")
        list_properties_parser.add_argument('groupid', help="Group id for which properties need to be listed", action='store')
        list_properties_parser.add_argument('productId', help="Product id for which properties need to be listed", action='store')
        list_properties_parser.add_argument('--output-type', '-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type {json, text}. Default is text')


        list_datasets_parser = subparsers.add_parser("list-datasets", help="List all Datasets.")
        list_datasets_parser.add_argument('--template', default='EDGE_LOGS', choices=['EDGE_LOGS'],help=' Template name for which datasets need to be fetched.[Example: EDGE_LOGS]')
        list_datasets_parser.add_argument('--output-type','-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type is json or text. Default is text')

        list_products_parser = subparsers.add_parser("list-products", help="List all Products.")
        list_products_parser.add_argument('--output-type','-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type is json or text. Default is text')

        get_stream_parser = subparsers.add_parser("get-stream", help="Get Details of Stream.")
        get_stream_parser.add_argument('streamid', help="Details of the stream", action='store')
        get_stream_parser.add_argument('--version','-v', default='latest',metavar='<latest>/<version id>', help='Version id to fetch. Default will be latest version.')
        get_stream_parser.add_argument('--output-type','-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type is json or text. Default is text')

        activation_history_parser = subparsers.add_parser("activation-history", help="Get Details of Stream Activation History.")
        activation_history_parser.add_argument('streamid', help="Stream ID", action='store')
        activation_history_parser.add_argument('--output-type','-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type is json or text. Default is text')

        stream_history_parser = subparsers.add_parser("stream-history", help="Get Details of Stream History.")
        stream_history_parser.add_argument('streamid', help="Stream ID", action='store')
        stream_history_parser.add_argument('--output-type','-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type is json or text. Default is text')

        '''
        list_error_streams_parser = subparsers.add_parser("list-error-streams", help="List all Errored Streams.")
        list_error_streams_parser.add_argument('groupid', help="Group id for which error streams need to be retrieve", action='store')
        list_error_streams_parser.add_argument('--output-type','-t', default='text', choices=['json', 'text'],metavar='json/text', help=' Output type is json or text. Default is text')
        '''

        create_stream_parser = subparsers.add_parser("create", help="Create a Particular Stream.")
        create_stream_parser.add_argument('file', help="Json File consiting of Stream Details", type=argparse.FileType('r'))

        update_stream_parser = subparsers.add_parser("update", help="Update a Particular Stream.")
        update_stream_parser.add_argument('streamid', help="Stream ID", action='store')
        update_stream_parser.add_argument('file', help="Json File consiting of Stream Details", type=argparse.FileType('r'))

        activation_parser = subparsers.add_parser("activate", help="Activate a Particular Stream.")
        activation_parser.add_argument('streamid', help="Stream ID", action='store')

        deactivation_parser = subparsers.add_parser("deactivate", help="Deactivate a Particular Stream.")
        deactivation_parser.add_argument('streamid', help="Stream ID", action='store')

        deletion_parser = subparsers.add_parser("delete", help="Delete a Particular Stream.")
        deletion_parser.add_argument('streamid', help="Stream ID", action='store')

        if flags:
            for argument in flags.keys():
                parser.add_argument('--' + argument, action=flags[argument])

        arguments = {}
        for argument in config_values:
            if config_values[argument]:
                if config_values[argument] == "False" or config_values[argument] == "True":
                    parser.add_argument('--' + argument, action='count')
                parser.add_argument('--' + argument)
                arguments[argument] = config_values[argument]

        try:
            args = parser.parse_args()
        except:
            sys.exit()

        arguments = vars(args)

        if arguments['debug']:
            http_client.HTTPConnection.debuglevel = 1
            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True


        if "section" in arguments and arguments["section"]:
            configuration = arguments["section"]

        arguments["edgerc"] = os.path.expanduser(arguments["edgerc"])

        if os.path.isfile(arguments["edgerc"]):
            config = ConfigParser()
            config.readfp(open(arguments["edgerc"]))
            if not config.has_section(configuration):
                err_msg = "ERROR: No section named %s was found in your %s file\n" % (configuration, arguments["edgerc"])
                err_msg += "ERROR: Please generate credentials for the script functionality\n"
                err_msg += "ERROR: and run 'python gen_edgerc.py %s' to generate the credential file\n" % configuration
                sys.exit( err_msg )
            for key, value in config.items(configuration):
                # ConfigParser lowercases magically
                if key not in arguments or arguments[key] is None:
                    arguments[key] = value
                else:
                    print("Missing configuration file.  Run python gen_edgerc.py to get your credentials file set up once you've provisioned credentials in LUNA.")
                    return None

        for option in arguments:
            setattr(self, option, arguments[option])

        self.create_base_url()

    def create_base_url(self):
        self.base_url = "https://%s" % self.host
