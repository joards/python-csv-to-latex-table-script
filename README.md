# python-csv-to-latex-table-script
Simple script which takes a csv file and outputs a latex table to stdout


Tested with python version 2.7.5

## Usage:
    $ python csv2latextable.py -i example1.csv
Writes to stdout a latex table based on example1.csv
Add the flag "-h" to get more info about user selectable parameters.

```
python csv2latextable.py -h
usage: csv2latextable.py [-h] [-i INPUTFILE] [-d DELIMITER] [-q QUOTECHAR]
                         [-pos TABLEPOS] [-caption CAPTION] [-lable REFLABLE]
                         [--underline]

Csv to latex table converter.

optional arguments:
  -h, --help        show this help message and exit
  -i INPUTFILE      Csv file to read, default=example1.csv
  -d DELIMITER      Set csv delimiter, default=;
  -q QUOTECHAR      Set csv quotechar, default="
  -pos TABLEPOS     Set table position, default=htbp
  -caption CAPTION  Set table caption, default='Generated table'
  -lable REFLABLE   Set table reference lable, default=''
  --underline       Add underline for each new entry
```

