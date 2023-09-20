# Directory Enumerator

This is a basic Python script for enumerating directories by sending HTTP requests to a target URL.

## How to Use

1. Create a file named `wordlist.txt` and add the directory paths you want to enumerate. Each directory path should be on a separate line.

2. Run the script with the following command:
```bash
python directory_enumerator.py example.com
```
Here, example.com is the target URL you want to scan. The script will generate URLs like http://example.com/directory.html and check if they return a 404 status code. If a 404 status code is not returned, it will print the URL to the console.

### Requirements
This script requires the following Python libraries:
  * requests
You can install this library using the following command:
```bash
pip install requests
```

### Notes
This script is a basic directory enumerator and may not cover all possible cases. More advanced directory enumeration tools are available for comprehensive scanning.
If a directory returns a 404 status code, the script will skip it and not print any output.
Ensure that you have proper authorization and permission to scan the target URL. Unauthorized scanning may be illegal in some cases.
