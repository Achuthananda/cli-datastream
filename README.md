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
This displays the usage of CAC akamai CLI.
```
$akamai ds --help
usage: akamai-datastream [-h] [--verbose] [--debug]
                         [--edgerc credentials_file]
                         [--section credentials_file_section]
                         [--accountSwitchKey Account Switch Key]
                         {list-groups,list-connectors} ...

Process command line options.

positional arguments:
  {list-groups,list-connectors}
                        commands
    list-groups         List all Groups in the Account
    list-connectors     List all Connectors Available. One of the connector
                        can be used as destination.

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
