import math
import os
import random
import json
import requests

import sys
import re

num = 9999
min = 0
for val in range(num,0,-1):
    s = str(val)
    result = val
    for ch in s:
        result += int(ch)

    if result == num:
        min = val

print(min)