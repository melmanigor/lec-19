import re
import unittest
hour="2459:30"
x=re.findall("^[0-2][0-4]:[0-5][0:9]:[0-5][0-9]$",hour)
print(x)