import math
import os
import random
import re
import sys
import json


a , b = map(int,input().split())

list = []

for _ in range(a):
    list.append(input())

result = sys.maxsize
for i in range(a-7):
    for j in range(b-7):
        start = 'B'
        wCount = 0
        bCount = 0
        for line in list[i:i+8]:
            for ch in line[j:j+8]:
                if ch != start:
                    bCount += 1

                if start == 'B':
                    start = 'W'
                else:
                    start = 'B'

            if start == 'B':
                start = 'W'
            else:
                start = 'B'

        start = 'W'
        for line in list[i:i+8]:
            for ch in line[j:j+8]:
                if ch != start:
                    wCount += 1

                if start == 'B':
                    start = 'W'
                else:
                    start = 'B'

            if start == 'B':
                start = 'W'
            else:
                start = 'B'

        result = min(result,(min(wCount, bCount)))

print(result)