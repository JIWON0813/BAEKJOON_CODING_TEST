import math
import os
import random
import json
import requests

import sys
import re

n = 19

x = 1
cnt = 1
while n > x:
    x += cnt*6
    cnt += 1

print(cnt)
