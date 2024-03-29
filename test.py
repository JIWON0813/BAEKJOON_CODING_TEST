import math
import os
import random
import json
import requests

import sys
import re
import heapq

get = int(input())
heap = []
for _ in range(get):
    val = int(input())

    if val == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, val)

    
