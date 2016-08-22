#!/bin/bash -l

#SBATCH -p debug 
#SBATCH -N 4
#SBATCH -t 00:30:00

d=/project/projectdirs/m349/cws/ace3p/bin/
acd=$d/acdtool
exes=($d/omega3p $d/omega3p_pumi)
names=(omega3p omega3p_pumi)

#srun $opts -n 1 $acd meshconvert cav17f.gen
len=${#exes[@]}
for((i=0;i<len;i++)); do
  exe=${exes[$i]}
  name=${names[$i]}
  echo $exe $name
  for p in 32 64 128; do 
    for j in {1..3}; do 
      echo $name $p $j noreorder
      srun $opts -n $p $exe crab.o3p.in.no-reorder
      mv omega3p_results ${name}_results_noreorder_${p}_${j}
    done
    for j in {1..3}; do 
      echo $name $p $j
      srun $opts -n $p $exe crab.o3p.in
      mv omega3p_results ${name}_results_${p}_${j}
    done
  done
done
