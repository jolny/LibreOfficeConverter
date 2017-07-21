# LibreOfficeConverter
A "lightweight" python script which converts XLS files to XLSX using Libre Office in headless mode.

## Prerequisites

* Python 2.x or 3.x
* Libre Office ;)

Tested on Ubuntu

## Usage

### Quick stand-alone conversion
To convert a set of XLS files to XLSX, run the script as such:
`python LibreOfficeConverter.py **files`

If no files are specified, the script will convert all files in the current working directory.

### Run from another Python app
Simple usage in another python application (provided script is in path or same folder):
```python
from LibreOfficeConverter import LibreOfficeConverter
converter = LibreOfficeConverter()
converter.to_xlsx()
```

Optional arguments:
* `verbose`
Whether to print output from LibreOffice. Default value: False
* `files`
Files to convert. If empty list, convert all in cwd. Default value: []
