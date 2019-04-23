# ccode_replace_python
# Python translation of Clayton Thyne's replace_ccode_country.do stata file
##JELambert Forked with updates

This script allows python users to utilize Clayton Thyne's Stata file for creating ccodes in country-level datasets. Allows for easy merging. Uses a modified text file of original stata code to scrape ccode numbers and country name strings.

**UPDATE 2/27/2018: Added 13 additional non-uniform country strings based on NAP dataset. The changes are reflected in the clthyn.txt file**

**Update 4/23/2019: Made the package distributable, removed unnecessary argument.**

# Credit for ccode/country information goes to Dr. Clayton Thyne at Kentucky. Process based on original .do file made by Thyne. See http://www.uky.edu/~clthyn2/research.htm for more information.

## Installation:
* Clone into a directory

* Navigate to ccode_replace_python/

* python setup.py install


## Example code

```
from ccode_replace_python import replace_ccode_country as rcc

df = ccode_make(df, 'country')


```
## Argument key

ccode_make(df, c_var)

1. df = your data frame
2. c_var = the original country string variable name from your df
