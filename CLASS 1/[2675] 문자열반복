import sys

for line in sys.stdin:
    if line == '\n':
        break
    
    line = line.replace('\n','')
    
    if ' ' not in line:
        continue
    
    a,b = line.split()
    num = int(a)
    newStr = ""
    for ch in b:
        for _ in range(num):
            newStr += ch
        
    print(newStr)
