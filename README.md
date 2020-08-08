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
$akamai cac [global flags] Commands
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
