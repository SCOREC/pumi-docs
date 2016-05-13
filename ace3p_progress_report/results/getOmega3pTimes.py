#!/usr/bin/env python3
import sys
import re

keys={ \
'Number of MPI processes:': -1, \
'Number of compute nodes:': -1, \
'Number of processes per node:': -1, \
'Time for setting up finite element framework:':-1, \
'Analysis step:': -2, \
'Factorization step:': -2, \
'used mem per MPI process:.*max:': 9, \
'used mem per MPI process:.*avg': 12, \
'Linear Solver Preparation Time:':-1, \
'Solver Time:': -1, \
'Omega3p ran in': -2 ,\
'planned Zoltan balance to target imbalance': -2 ,\
'Zoltan balanced to': -2 ,\
'PARMA_STATUS ghosts balanced in \d* steps': 4 ,\
'PARMA_STATUS ghosts balanced in \d* steps to': 7 ,\
'PARMA_STATUS ghosts balanced in \d* steps to \d*.\d* in': -2 ,\
'Parma time to read': -1 ,\
'Parma time to convert shape': -1 ,\
'Parma time to convert to DM': -1 ,\
'Time for reading the model': -1 ,\
'Time for checking the mesh quality': -1 ,\
'Time for save/load ComputationalMesh': -1 \
}

#'Parma time to balance w/ zoltan': -1 ,\
#'Parma time to balance w/ ghosting': -1 ,\


def printlog(log):
    for k in sorted(log.keys()):
        print(k,',',log[k])

if len(sys.argv) is not 2:
    print('Usage: ', sys.argv[0], ' <omega3p output file>')
    sys.exit()

print('file',',',sys.argv[1])
f = open(sys.argv[1],'r')

log = {}
for line in f:
    for k,v in keys.items():
        m = re.search(k, line)
        if m:
            #print(line,end='')
            log[k] = line.split()[v]
    if line.startswith('ACE3P git repo hash'):
        printlog(log)
f.close()
printlog(log)
