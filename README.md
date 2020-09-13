# Akamai CLI: DataStream 2.0 Module

This module enables the use of DataStream in the Akamai CLI tool

## API Permissions

Please ensure your API client has access to the "DataStream" API (you may need to create a separate API client)

## Install

To install, use [Akamai CLI](https://github.com/akamai/cli):

```
$akamai install https://github.com/Achuthananda/cli-datastream.git
```

You may also use this as a stand-alone command by cloning this repository
and compiling it yourself.

## Usage

```
$akamai datastream [global flags] Commands
```

## Global Flags
- `--edgerc value` — Location of the credentials file (default: user's directory like "/Users/apadmana") [$AKAMAI_EDGERC]
- `--section value` — Section of the credentials file (default: "default") [$AKAMAI_EDGERC_SECTION]
- `--debug` - `-d` - prints debug information
- `--verbose` - Print verbose information
- `--version`, `-v` — Print the version
- `--help`, `-h` — Show help

## Commands  
- `list-groups` —   List all Groups in the Account
- `list-connectors` — List all Connectors Available.


## Examples

#### Help
This displays the usage of Datastream Akamai CLI.
```
$akamai ds --help
usage: akamai-datastream [-h] [--verbose] [--debug]
                         [--edgerc credentials_file]
                         [--section credentials_file_section]
                         [--accountSwitchKey Account Switch Key]
                         {list-groups,list-connectors,list-stream-types,list-streams,list-properties,list-datasets,list-products,get-stream,activation-history,stream-history,create,update,activate,deactivate,delete}
                         ...

Process command line options.

positional arguments:
  {list-groups,list-connectors,list-stream-types,list-streams,list-properties,list-datasets,list-products,get-stream,activation-history,stream-history,create,update,activate,deactivate,delete}
                        commands
    list-groups         List all Groups in the Account
    list-connectors     List all Connectors.
    list-stream-types   List all Types of Stream.
    list-streams        List all Streams.
    list-properties     List all Properties.
    list-datasets       List all Datasets.
    list-products       List all Products.
    get-stream          Get Details of Stream.
    activation-history  Get Details of Stream Activation History.
    stream-history      Get Details of Stream History.
    create              Create a Particular Stream.
    update              Update a Particular Stream.
    activate            Activate a Particular Stream.
    deactivate          Deactivate a Particular Stream.
    delete              Delete a Particular Stream.

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         Verbose mode
  --debug, -d           Debug mode (prints HTTP headers)
  --edgerc credentials_file, -e credentials_file
                        Location of the credentials file (default is
                        ~/.edgerc)
  --section credentials_file_section, -c credentials_file_section
                        Credentials file Section's name to use
  --accountSwitchKey Account Switch Key, -a Account Switch Key
                        Switch key to different account
```

#### Usage of list-groups Command
This shows how to use list-groups.
```
$ akamai ds list-groups- -h
          [or]
$ akamai ds list-groups --help
usage: akamai-datastream list-groups [-h] [--output-type json/text]

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```


#### List All the Groups in the Account
This shows all the Groups in the Account.
```
$ akamai datastream list-groups
+---------------------------+--------------------------------+
|         Group Id          |           Group Name           |
+===========================+================================+
|          103489           |        Edgeconnect Lab         |
+---------------------------+--------------------------------+
|          141474           |           mPulse Lab           |
+---------------------------+--------------------------------+
|          118499           |  DevPoPs Demo - Please do not  |
|                           |              edit              |
+---------------------------+--------------------------------+
```

#### List All the Groups in the Account in Json Format
This shows all the groups in the Account in Json Format.
```
$ akamai datastream list-groups --output-type json
[
  {
    "parentGroupId": 48668,
    "contractIds": [
      "3-16TWBVX"
    ],
    "childGroupIds": [],
    "groupId": 103489,
    "groupName": "Edgeconnect Lab",
    "description": null,
    "accountId": "B-3-16OEUPX",
    "enabled": true,
    "childGroups": []
  },
  {
    "parentGroupId": 48668,
    "contractIds": [
      "3-16TWBVX"
    ],
    "childGroupIds": [],
    "groupId": 141474,
    "groupName": "mPulse Lab",
    "description": null,
    "accountId": "B-3-16OEUPX",
    "enabled": true,
    "childGroups": []
  },
  {
    "parentGroupId": 48668,
    "contractIds": [
      "3-16TWBVX"
    ],
    "childGroupIds": [],
    "groupId": 118499,
    "groupName": "DevPoPs Demo - Please do not edit",
    "description": null,
    "accountId": "B-3-16OEUPX",
    "enabled": true,
    "childGroups": []
  }
]
```

#### Usage of list-connectors Command
This shows how to use list-connectors command.
```
$ akamai ds list-connectors -h
          [or]
$ akamai ds list-connectors --help
usage: akamai datastream list-connectors [-h] [--output-type json/text]

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```


#### List of all Connectors.
Retrieve a list of all supported Connectors or End Points
```
$ akamai datastream list-connectors
+---------------------------+--------------------------------+
|     ConnectorType Id      |       ConnectorType Name       |
+===========================+================================+
|             7             |         Azure Storage          |
+---------------------------+--------------------------------+
|             2             |               S3               |
+---------------------------+--------------------------------+
```


#### Usage of list-streams Command
This shows how to use list-streams command to get the list of streams in a group.
```
$ akamai ds list-streams -h
          [or]
$ akamai ds list-streams --help
usage: akamai datastream list-streams [-h] [--output-type json/text] groupid

positional arguments:
  groupid               Group id for which streams need to be retrieve

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type is json or text. Default is text

```

#### List of all Streams in a group.
Retrieve a list of all streams in a group.
```
$ akamai datastream list-streams 173720
+----------+----------------------+-----------------+---------------------------+----------------------+--------------+
| StreamId |      StreamName      |    CreatedBy    |        Properties         |      Connectors      |    Status    |
+==========+======================+=================+===========================+======================+==============+
|   5680   |   OPEN API testing   |    mrangasw     |     ogravier.betajam-     |  Azure Storage-Auto  | DEACTIVATED  |
|          |                      |                 |     dstream.fun_clone     |        FIlled        |              |
+----------+----------------------+-----------------+---------------------------+----------------------+--------------+
|   5670   |    dgarg_betajam     |      dgarg      |   betajam-dstream-dgarg   |   S3-dgarg_betajam   |  ACTIVATED   |
+----------+----------------------+-----------------+---------------------------+----------------------+--------------+

```


#### Usage of get-stream Command
This shows how to use get-stream command to get the details of a stream in a group.
```
$ akamai ds get-stream -h
          [or]
$ akamai ds get-stream --help
usage: akamai datastream get-stream [-h] [--version <latest>/<version id>]
                                    [--output-type json/text]
                                    streamid

positional arguments:
  streamid              Details of the stream

optional arguments:
  -h, --help            show this help message and exit
  --version <latest>/<version id>, -v <latest>/<version id>
                        Version id to fetch. Default will be latest version.
  --output-type json/text, -t json/text
                        Output type is json or text. Default is text

```

#### Get the details of a stream.
Retrieve the details of a stream.
```
$ akamai datastream get-stream 5665

Stream Id: 5665
Stream Name: achuth-ds2betajam
Stream Version: 1
Stream Type: RAW_LOGS
Connector Name: achuth-s3ds2
Connector Type: S3
Product Name: Adaptive_Media_Delivery
Upload Frequency(in secs): 30
Created By: apadmana
Datasets Selected:
+---------------------------+------------+---------------------------+-------------------------------------+
|        Group Name         |  Field Id  |        Field Name         |          Field Description          |
+===========================+============+===========================+=====================================+
|      Log information      |    1000    |          CP Code          |  Content Provider Code associated   |
|                           |            |                           |            with Request             |
+---------------------------+------------+---------------------------+-------------------------------------+
|      Log information      |    1002    |        Request ID         |  The request identifier associated  |
|                           |            |                           |            with request             |
+---------------------------+------------+---------------------------+-------------------------------------+
|      Log information      |    1100    |       Request Time        |      Start time of the request      |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1005    |           Bytes           |   The content bytes served in the   |
|                           |            |                           |           client response           |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1006    |         Client IP         |  The IP address of the requesting   |
|                           |            |                           |               client                |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1008    |     HTTP Status Codes     |  The HTTP Response status sent to   |
|                           |            |                           |             the client              |
+---------------------------+------------+---------------------------+-------------------------------------+
```

#### Get the details of a Specific version of a stream.
Retrieve the details of a specific version of a stream.
```
$ akamai datastream get-stream 5665 -v 2
Stream Id: 5665
Stream Name: achuth-ds2betajam
Stream Version: 2
Stream Type: RAW_LOGS
Connector Name: achuth-s3ds2
Connector Type: S3
Product Name: Adaptive_Media_Delivery
Upload Frequency(in secs): 30
Created By: apadmana
Datasets Selected:
+---------------------------+------------+---------------------------+-------------------------------------+
|        Group Name         |  Field Id  |        Field Name         |          Field Description          |
+===========================+============+===========================+=====================================+
|      Log information      |    1000    |          CP Code          |  Content Provider Code associated   |
|                           |            |                           |            with Request             |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1006    |         Client IP         |  The IP address of the requesting   |
|                           |            |                           |               client                |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1008    |     HTTP Status Codes     |  The HTTP Response status sent to   |
|                           |            |                           |             the client              |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           |   The protocol of the transaction   |
|   Message exchange data   |    1009    |       Protocol Type       | being monitored. Currently HTTP or  |
|                           |            |                           |               HTTPS.                |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1011    |       Request Host        | The value of the Host header of the |
|                           |            |                           |       incoming client request       |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           | The method of the incoming request  |
|   Message exchange data   |    1012    |      Request Method       |   - assuming an HTTP request. For   |
|                           |            |                           |  example: GET, POST, PUT, and HEAD  |
+---------------------------+------------+---------------------------+-------------------------------------+
```

#### Usage of activation-history Command
This shows how to use activation-history command to get the details of activation history of a stream .
```
$ akamai ds activation-history -h
          [or]
$ akamai ds activation-history --help
uusage: akamai-datastream activation-history [-h] [--output-type json/text]
                                            streamid

positional arguments:
  streamid              Stream ID

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type is json or text. Default is text

```


#### List the Activation History of a Stream.
This command gives the details of activation history of a stream.
```
$ akamai datastream activation-history 5665
+----------+-----------+-----------------+---------------------------+-----------------+
| StreamId | VersionId |    CreatedBy    |       Created Date        |     Status      |
+==========+===========+=================+===========================+=================+
|   5665   |     2     |    apadmana     |  08-08-2020 14:00:43 GMT  |     Active      |
+----------+-----------+-----------------+---------------------------+-----------------+
|   5665   |     1     |    apadmana     |  05-08-2020 17:31:17 GMT  |     Active      |
+----------+-----------+-----------------+---------------------------+-----------------+
|   5665   |     1     |    apadmana     |  05-08-2020 15:41:29 GMT  |    Inactive     |
+----------+-----------+-----------------+---------------------------+-----------------+

```


#### Usage of list-stream-types Command
This shows how to use list-stream-types command.
```
$ akamai ds list-stream-types -h
          [or]
$ akamai ds list-stream-types --help
usage: akamai-datastream list-stream-types [-h] [--output-type json/text]

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```


#### List of all Stream Types.
Get the list of all types of streams available.
```
$ akamai datastream list-stream-types
+--------------+----------------+----------------------+------------+----------+
| StreamTypeId | StreamTypeName | StreamTypeIdentifier |  Delivery  |   Raw    |
+==============+================+======================+============+==========+
|      3       |    2.0 BETA    |       RAW_LOGS       |    Log     |   Yes    |
+--------------+----------------+----------------------+------------+----------+
```

#### List of all Products.
Get the list of all types of Products, Products Ids and groups it is available.
```
$ akamai datastream list-products
+----------------------+---------------------------+---------------------------+-----------------+
|       Product        |        Product Id         |          Groups           |    Templates    |
+======================+===========================+===========================+=================+
|                      |                           |   [48668, 73337, 84517,   |                 |
|     Ion Standard     |       Ion_Standard        |  93139, 103415, 103489,   |  ['EDGE_LOGS']  |
|                      |                           |  106598, 117609, 118499,  |                 |
|                      |                           |      141474, 173720]      |                 |
+----------------------+---------------------------+---------------------------+-----------------+
|                      |                           |   [48668, 73337, 84517,   |                 |
|     Ion Premier      |        Ion_Premier        |  93139, 103415, 103489,   |  ['EDGE_LOGS']  |
|                      |                           |  106598, 117609, 118499,  |                 |
|                      |                           |      141474, 173720]      |                 |
+----------------------+---------------------------+---------------------------+-----------------+
|                      |                           |   [48668, 73337, 84517,   |                 |
|     Dynamic Site     | Dynamic_Site_Accelerator  |  93139, 103415, 103489,   |  ['EDGE_LOGS']  |
|     Accelerator      |                           |  106598, 117609, 118499,  |                 |
|                      |                           |      141474, 173720]      |                 |
+----------------------+---------------------------+---------------------------+-----------------+
|                      |                           |   [48668, 73337, 84517,   |                 |
|  Ion Media Advanced  |    Ion_Media_Advanced     |  93139, 103415, 103489,   |  ['EDGE_LOGS']  |
|                      |                           |  106598, 117609, 118499,  |                 |
|                      |                           |      141474, 173720]      |                 |
+----------------------+---------------------------+---------------------------+-----------------+
|                      |                           |   [48668, 73337, 84517,   |                 |
|    Adaptive Media    |  Adaptive_Media_Delivery  |  93139, 103415, 103489,   |  ['EDGE_LOGS']  |
|       Delivery       |                           |  106598, 117609, 118499,  |                 |
|                      |                           |      141474, 173720]      |                 |
+----------------------+---------------------------+---------------------------+-----------------+
|                      |                           |   [48668, 73337, 84517,   |                 |
|  Download Delivery   |     Download_Delivery     |  93139, 103415, 103489,   |  ['EDGE_LOGS']  |
|                      |                           |  106598, 117609, 118499,  |                 |
|                      |                           |      141474, 173720]      |                 |
+----------------------+---------------------------+---------------------------+-----------------+
```

#### Get the Stream History.
Retrieves the history of a stream. This takes stream ID as input
```
$akamai datastream stream-history <streamid>
```
```
$ akamai datastream stream-history 5665
------------------------------------------------------------------------------------------------------------------------------------------------------
Stream ID: 5665
Stream Version: 4
Stream Name: achuth-ds2betajam
Product Name Adaptive Media Delivery
DataSets:
Log information : ['Request ID', 'Request Time']
Message exchange data : ['Client IP', 'Request Method']
------------------------------------------------------------------------------------------------------------------------------------------------------
Stream ID: 5665
Stream Version: 3
Stream Name: achuth-ds2betajam
Product Name Adaptive Media Delivery
DataSets:
Log information : ['CP Code']
Message exchange data : ['Request Host', 'Client IP', 'Request Method', 'Request Path']
Request header data : ['Referer', 'Range']
Network performance data : ['Request End Time', 'Turn Around Time']
------------------------------------------------------------------------------------------------------------------------------------------------------
Stream ID: 5665
Stream Version: 2
Stream Name: achuth-ds2betajam
Product Name Adaptive Media Delivery
DataSets:
Log information : ['CP Code']
Message exchange data : ['Request Host', 'Client IP', 'Request Method', 'HTTP Status Codes', 'Request Path', 'Protocol Type', 'Total Bytes']
Request header data : ['Referer', 'Range']
Network performance data : ['Request End Time', 'Turn Around Time']
------------------------------------------------------------------------------------------------------------------------------------------------------
Stream ID: 5665
Stream Version: 1
Stream Name: achuth-ds2betajam
Product Name Adaptive Media Delivery
DataSets:
Log information : ['CP Code', 'Request ID', 'Request Time']
Message exchange data : ['Bytes', 'Request Host', 'Response Content Length', 'Client IP', 'Request Method', 'Response Content Type', 'HTTP Status Codes', 'Request Path', 'User-Agent', 'Protocol Type', 'Request Port', 'Total Bytes']
Request header data : ['Accept-Language', 'X-Forwarded-For', 'Cookie', 'Range', 'Referer']
Network performance data : ['Request End Time', 'Transfer Time', 'Error Code R14', 'Turn Around Time']
------------------------------------------------------------------------------------------------------------------------------------------------------

```

#### Get the Datasets Available
Retrieves the list of datasets for a particular template.
```
$akamai datastream list-datasets --template <templatename>
```
```
$ akamai datastream list-datasets --template EDGE_LOGS
+---------------------------+------------+---------------------------+-------------------------------------+
|        Group Name         |  Field Id  |        Field Name         |          Field Description          |
+===========================+============+===========================+=====================================+
|      Log information      |    1000    |          CP Code          |  Content Provider Code associated   |
|                           |            |                           |            with Request             |
+---------------------------+------------+---------------------------+-------------------------------------+
|      Log information      |    1002    |        Request ID         |  The request identifier associated  |
|                           |            |                           |            with request             |
+---------------------------+------------+---------------------------+-------------------------------------+
|      Log information      |    1100    |       Request Time        |      Start time of the request      |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1005    |           Bytes           |   The content bytes served in the   |
|                           |            |                           |           client response           |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1006    |         Client IP         |  The IP address of the requesting   |
|                           |            |                           |               client                |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1008    |     HTTP Status Codes     |  The HTTP Response status sent to   |
|                           |            |                           |             the client              |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           |   The protocol of the transaction   |
|   Message exchange data   |    1009    |       Protocol Type       | being monitored. Currently HTTP or  |
|                           |            |                           |               HTTPS.                |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1011    |       Request Host        | The value of the Host header of the |
|                           |            |                           |       incoming client request       |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           | The method of the incoming request  |
|   Message exchange data   |    1012    |      Request Method       |   - assuming an HTTP request. For   |
|                           |            |                           |  example: GET, POST, PUT, and HEAD  |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           |  The path used in the incoming URI  |
|   Message exchange data   |    1013    |       Request Path        |   from the client, not including    |
|                           |            |                           |            query strings            |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1014    |       Request Port        |   The port number of the incoming   |
|                           |            |                           |           client request            |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1015    |  Response Content Length  |   The value of the Content-Length   |
|                           |            |                           |    header in the client response    |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1016    |   Response Content Type   |    The value of the Content-Type    |
|                           |            |                           |    header in the client request     |
+---------------------------+------------+---------------------------+-------------------------------------+
|   Message exchange data   |    1017    |        User-Agent         | The value of the User-Agent header  |
|                           |            |                           |        in the client request        |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           |  The total bytes served in client   |
|   Message exchange data   |    1101    |        Total Bytes        |  response including content & HTTP  |
|                           |            |                           |              overhead               |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           | Provides a list of acceptable human |
|    Request header data    |    1019    |      Accept-Language      |     languages for response. For     |
|                           |            |                           | example, American English is en-US  |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           |  Lists the HTTP cookie previously   |
|    Request header data    |    1023    |          Cookie           |   sent by the server in the Set-    |
|                           |            |                           |               Cookie                |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           |   Requests a specific part of an    |
|    Request header data    |    1031    |           Range           |  entity by providing a single byte  |
|                           |            |                           |   range or a set of byte ranges.    |
|                           |            |                           |     Bytes are numbered from 0.      |
+---------------------------+------------+---------------------------+-------------------------------------+
|    Request header data    |    1032    |          Referer          |  Lists the resource from which the  |
|                           |            |                           |     requested URI was obtained      |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           |    Identifies the originating IP    |
|    Request header data    |    1037    |      X-Forwarded-For      | address of a client connecting to a |
|                           |            |                           | web server through an HTTP proxy or |
|                           |            |                           |            load balancer            |
+---------------------------+------------+---------------------------+-------------------------------------+
| Network performance data  |    1033    |     Request End Time      |  Provides the time of the request   |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           |  If there is an error serving the   |
| Network performance data  |    1068    |      Error Code R14       |   request a string indicating the   |
|                           |            |                           |       problem is logged here.       |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           |  The time in milliseconds between   |
|                           |            |                           |  receipt of the end of the request  |
| Network performance data  |    1102    |     Turn Around Time      | headers and when the first byte of  |
|                           |            |                           | the reply is written to the client  |
|                           |            |                           |               socket                |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           | The time in milliseconds it took to |
|                           |            |                           |  send the response to the client,   |
| Network performance data  |    1103    |       Transfer Time       | measured from the time Akamai Edge  |
|                           |            |                           | was ready to send the first byte to |
|                           |            |                           |     when it sent the last byte.     |
+---------------------------+------------+---------------------------+-------------------------------------+
|                           |            |                           | contains the value specified by the |
|                           |            |                           | metadata tag reporting:lds.custom-  |
|           Other           |    1082    |       Custom Field        | field. Note that, the tag can (and  |
|                           |            |                           | generally would) take an extracted  |
|                           |            |                           |   variable as its content, so the   |
|                           |            |                           |  value of this field is not fixed.  |
+---------------------------+------------+---------------------------+-------------------------------------+
```

#### Activate a Stream.
This Command will activate a stream.
```
$akamai datastream activate <stream id>
```
```
$ akamai datastream activate 5669
{
  "streamVersionKey": {
    "streamId": 5669,
    "streamVersionId": 1
  }
}
```

#### Deactivate a Stream.
This Command will deactivate a stream.
```
$akamai datastream deactivate <stream id>
```
```
$ akamai datastream deactivate 6305
{
  "streamVersionKey": {
    "streamId": 6305,
    "streamVersionId": 1
  }
}
```

#### List all properties of a product type in a group .
This Command will list all properties of a product type in a group
```
$akamai datastream list-properties <groupdId> <productId>
```
```
$ akamai datastream list-properties 173720 Adaptive_Media_Delivery
+----------+--------------------------------+
| Property |          PropertyName          |
|    Id    |                                |
+==========+================================+
|  632446  |    amd_template.techjam.fun    |
+----------+--------------------------------+
|  638300  |   damin.betajam-dstream-amd    |
+----------+--------------------------------+
|  639714  |   tblackfo.techjam.fun_clone   |
+----------+--------------------------------+
|  639728  |    betajam-dstream-smacleod    |
+----------+--------------------------------+
|  639731  |    etajam-dstream-heerikss     |
+----------+--------------------------------+
|  639732  |    betajam-dstream-gethilka    |
+----------+--------------------------------+
|  639737  |      fdiazsav.techjam.fun      |
+----------+--------------------------------+
|  639738  | apadmana-amd_template.techjam  |
+----------+--------------------------------+
|  639753  |     sammy.betajam-dstream      |
+----------+--------------------------------+
|  639754  |       ogravier.betajam-        |
|          |       dstream.fun_clone        |
+----------+--------------------------------+
|  645893  |    betajam-dstream-jtokimit    |
+----------+--------------------------------+
|  645896  |   aphilip.techjam.fun_clone    |
+----------+--------------------------------+
|  648514  | apadmana-amd_template1.techjam |
+----------+--------------------------------+
|  648528  |           apadmana-            |
|          |  amd_template3.techjam_clone   |
+----------+--------------------------------+
|  648529  | apadmana-amd_template2.techjam |
+----------+--------------------------------+
```

#### Create a Stream.
This CLI will create a stream. This command expects a json file in the same directory and the format is available in create_template.json file.
```
$akamai datastream create <json_file_name>
```
Create json file format is shown below.
```
{
  "streamName": "test-ds-jam",
  "activateNow": false,
  "streamType": "RAW_LOGS",
  "productId": "Adaptive_Media_Delivery",
  "templateName": "EDGE_LOGS",
  "groupId": 12373asd720,
  "groupName": "DS2 Beta Jam",
  "contractId": "3-16TSLSLWBVX",
  "propertyIds": [
        641134528
  ],
  "datasetFieldIds": [
        1000,
        1002,
        1100
  ],
  "config": {
    "delimiter": "COMMA",
    "uploadFilePrefix": "ak",
    "uploadFileSuffix": "ds",
    "frequency": {
      "timeInSec": 30,
      "sizeInMb": 4,
      "numberOfRecords": 32000
    },
    "useStaticPublicIP": false
  },
  "connectors": [
    {
      "compressLogs": true,
      "path": "apadmaasdsadna/",
      "connectorName": "achuasdsadth-s3ds2",
      "bucket": "ds2betasdsadajam",
      "region": "us-east-1",
      "accessKey": "acess_key",
      "secretAccessKey": "secret_key",
      "connectorType": "S3"
    }
  ],
  "emailIds": "apadmasasasdfdfana@akamai.com"
}
```
```
$ akamai datastream create create.json
{
  "streamVersionKey": {
    "streamId": 6454,
    "streamVersionId": 1
  }
}
```

#### Update a Stream.
This CLI will update a stream. This command expects stream id and a json file in the same directory and the format is available in update_template.json file. This command will also auto publish the stream.
```
$akamai datastream update <streamId> <json_file_name>
```
Update json file format is shown below.
```
{
    "streamName": "achuth-dasdsads2betajam",
    "streamType": "RAW_LOGS",
    "templateName": "EDGE_LOGS",
    "contractId": "3-16TWBVX",
    "propertyIds": [
        6397asdsa38
    ],
    "datasetFieldIds": [
        1002,
        1100,
        1006,
        1012
    ],
    "config": {
        "delimiter": "COMMA",
        "uploadFilePrefix": "ak",
        "uploadFileSuffix": "amai",
        "frequency": {
            "timeInSec": 30,
            "sizeInMb": 4,
            "numberOfRecords": 32000
        }
    },
    "emailIds": "apadasdsmana@example.com"
}
```
```
$ akamai datastream update 6454 update.json
{
  "streamVersionKey": {
    "streamId": 6454,
    "streamVersionId": 2
  }
}
```

#### Delete a Stream.
This CLI will delete a stream. The stream should be in deactivated state.
```
$akamai datastream delete <streamId>
```
```
$ akamai datastream delete 6455
{
  "message": "Success"
}
```
```
$akamai datastream delete 6455
{
  "type": "bad-request",
  "title": "Bad Request",
  "instance": "790778d4-e130-4bbb-a329-44090e547985",
  "status": 400,
  "errors": [
    {
      "type": "bad-request",
      "title": "Bad Request",
      "detail": "Stream is already deleted.Please provide valid stream."
    }
  ]
}
```
```
$akamai datastream delete 6305
{
  "type": "bad-request",
  "title": "Bad Request",
  "instance": "26acb89e-a2fc-4439-9b15-d59f513e3811",
  "status": 400,
  "errors": [
    {
      "type": "bad-request",
      "title": "Bad Request",
      "detail": "Deactivation of stream is in progress. Stream can not be deleted."
    }
  ]
}
```
