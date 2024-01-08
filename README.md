## Welcome 


## Key Functionality
- capture changes day-to-day to APFS records
    - Hash previous day records and compare to current day records
- Notify if key-words are found
- filter and display data for internal research purposes 
- Use pytest for testing 



## Pytest

When working with unit testing, it is important to keep in mind that the tests should be independent of each other. 

When running the tests you will type in the command line at the root directory of the project "pytest".

If you get an error like this: 

```
tests/test_apfs_scan.py:3: in <module>
    from apfs_scan import CustomHttpAdapter
E   ModuleNotFoundError: No module named 'apfs_scan' 
```

you will may need to run the command "pip install -e /path/to/project" to install the project. If you do not know the current working directory of your project, you can type into the command line "pwd" or "echo $PWD" and this will provide your working directory.

If you still see the error above, then you will need to insert this command into the terminal: "export PYTHONPATH=/path/to/project" and insert your current working directory into the path.
