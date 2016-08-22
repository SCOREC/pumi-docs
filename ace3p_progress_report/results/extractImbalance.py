#!/usr/bin/env python3
import sys
import re

if len(sys.argv) is not 2:
    print('Usage: ', sys.argv[0], ' <omega3p output file>')
    sys.exit()

print('file',',',sys.argv[1])
f = open(sys.argv[1],'r')

keys=["Local Elements","Ghost Elements","Total Elements","Local Vertices",\
      "Ghost Vertices", "Total Vertices"]

def printlog(log):
    for k in sorted(log.keys()):
        print(k,end=',')
        for i in log[k]:
           print(i,end=',')
        print()

def getStats(line):
    tokens = line.split()
    stats={}
    # 1      2       3    4    5   6    7     8    9     10       11   12
    #Local Elements Max 10426 Min 9245 Tot 318118 Avg 9941.000000 Imb 1.048788
    keys={"Max":3,"Min":5,"Tot":7,"Avg":9,"Imb":11}
    for k,v in keys.items():
        stats[k] = tokens[v]
    return stats

runs = []
log = {}
for line in f:
    if line.startswith('omega3p ') or line.startswith('omega3p_pumi '):
        log['exe'] = line.split()[0]
        log['cores'] = line.split()[1]
    for k in keys:
        m = re.search(k, line)
        if m:
            log[k] = getStats(line)
    if line.startswith('Omega3p peak memory usage'): #last line
        runs.append(log)
        log = {}
f.close()

def name(prefix,key):
    return prefix + ' ' + key

print('runs,',len(runs))
#initialize the output log - dictionary of lists
log = {}
log['exe'] = []
log['cores'] = []
for k in sorted(keys):
    for i,v in runs[0][k].items():
        log[name(k,i)] = []
#populate the output log
for run in runs:
    log['exe'].append(run['exe'])
    log['cores'].append(run['cores'])
    for k in sorted(keys):
        for i,v in run[k].items():
            log[name(k,i)].append(v)
printlog(log)
