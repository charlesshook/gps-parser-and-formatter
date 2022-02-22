# gps-parser-and-formatter
Wanted an easy way to get the latitude and longitude from a .csv that
I was trying to use for another project.

### Running The Program
```
    pip3 -r requirements.txt
    python3 main.py
```


### CSV File Format
As long as the .csv file has latitude and longitude as headers in the
file then this script should be able to grab it.

### Output Format
```
    prefix_(latitude)_delimiter_(longitude)_postfix
```

Here is an example:
```
    prefix =addPoint(
    delimiter =, 
    postfix =);
    
    addPoint(44.45466,-144.36485);
```