# DMP Analysis Script

Extracts the survey information from the Data Management Plan (DMP) Sufficiency Checklist into a text format using TAB delimited as separator.
The application provides the option to summarize/aggregate the information for multiple documents.

The application is using Python 3.x as primary programming language and should be able to be executed across operative systems.

## Usage

```shell
 python main.py [-h] [-o OUTPUT] [-d] PATH
```

* __-h , --help__
  * Print the command line help
* __-o, --output [output]__
  * Target location for the reported files.
* __-d, --detailed__
  * Generates a detailed report instead of the default summary report
* __PATH (Mandatory)__
  * DMP file name document or directory that contains the documents

## Configuration

The applications requires [Python 3.x](https://www.python.org/download/releases/3.0/) and the packages listed in the requirements.txt file.

## Installation
It is recommended to use a [virtualenv](https://virtualenv.pypa.io/en/latest/) to not pollute the local environment.

Copy or clone the application files into a directory and follow the next instructions

Use [pip](https://pypi.org/project/pip/) to install the requirements file (requirements.txt) using the following command

```shell
pip install -r requirements.txt
```

## File Manifest
* Python 3.x : https://www.python.org/download/releases/3.0
* lxml : https://pypi.org/project/lxml/
* python-docx : https://pypi.org/project/python-docx/


## Development setup
1. Copy or clone the application into a directory
2. Install the required packages
```shell
pip install -r requirements.txt
```
* Run the application
```shell
python main.py [-h] [-o OUTPUT] [-d] PATH
```
* Run Unit Test
```shell
 python -m unittest discover test
```

## Release History
* 0.1.0
  * Initial version


## Contact information
Joe Doe : X@Y

Distributed under XYZ license. See *LICENSE* for more information

## Contributing
1. Fork it (https://github.com/usdot-its-jpo-data-portal/dmp_analysis_script/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request

## Known Bugs
*

## Credits and Acknowledgment
Thank you to the Department of Transportation for funding to develop this project.

## CODE.GOV Registration Info
* __Agency:__ DOT
* __Short Description:__ Extracts the survey information from the Data Management Plan (DMP) Sufficiency Checklist into a text format using TAB delimited as separator.
* __Status:__ Beta
* __Tags:__ transportation, connected vehicles, intelligent transportation systems, python, DMP, Sufficiency Checklist
* __Labor Hours:__
* __Contact Name:__
* __Contact Phone:__
