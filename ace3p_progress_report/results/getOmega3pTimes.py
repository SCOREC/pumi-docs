#!/usr/bin/env python3
import sys
import re

keys={ \
'omega3p \d* \d* noreorder': 1, \
'omega3p \d* \d*$': 1, \
'omega3p_pumi \d* \d* noreorder': 1, \
'omega3p_pumi \d* \d*$': 1, \
'Number of MPI processes:': -1, \
'Number of compute nodes:': -1, \
'Number of processes per node:': -1, \
'Time for setting up finite element framework:':-1, \
'Analysis step:': -2, \
'Factorization step:': -2, \
'Linear Solver Preparation Time:':-1, \
'Solver Time:': -1, \
'Omega3p ran in': -2 ,\
'Omega3p peak memory usage': -1 ,\
'planned Zoltan balance to target imbalance': -2 ,\
'Zoltan balanced to': -2 ,\
'PARMA_STATUS ghostEdges balanced in \d* steps': 4 ,\
'PARMA_STATUS ghostEdges balanced in \d* steps to': 7 ,\
'PARMA_STATUS ghostEdges balanced in \d* steps to \d*.\d* in': -2 ,\
'Parma time to read': -1 ,\
'Parma time to convert shape': -1 ,\
'Parma time to convert to DM': -1 ,\
'Time for reading the model': -1 ,\
'Time for checking the mesh quality': -1 ,\
'Time for save/load ComputationalMesh': -1 \
}

def printlog(log):
    for k in sorted(log.keys()):
        print(k,end=',')
        for i in log[k]:
           print(i,end=',')
        print()

if len(sys.argv) is not 2:
    print('Usage: ', sys.argv[0], ' <omega3p output file>')
    sys.exit()

print('file',',',sys.argv[1])
f = open(sys.argv[1],'r')

runs = []
log = {}
for line in f:
    for k,v in keys.items():
        m = re.search(k, line)
        if m:
            log[k] = line.split()[v]
    if line.startswith('Omega3p peak memory usage'): #last line
        runs.append(log)
        log = {}
f.close()

log = {}
for k in sorted(keys):
    log[k] = []
print(len(runs))
for run in runs:
    for k in sorted(keys):
        if k in run:
          log[k].append(run[k])
        else:
          log[k].append('')

printlog(log)
