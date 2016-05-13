echo tot vtx
grep 'Total Vertices Max' slurm-2189328.imb.out | awk '{print $5}'
echo imb vtx
grep 'Total Vertices Max' slurm-2189328.imb.out | awk '{print $(NF)}'
echo tot elm
grep 'Total Elements Max' slurm-2189328.imb.out | awk '{print $5}'
echo imb elm
grep 'Total Elements Max' slurm-2189328.imb.out | awk '{print $(NF)}'
