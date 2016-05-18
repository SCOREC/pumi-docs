#!/bin/bash -e
log=$1
echo tot vtx
grep 'Total Vertices Max' $log | awk '{print $5}'
echo imb vtx
grep 'Total Vertices Max' $log | awk '{print $(NF)}'
echo ghost vtx
grep 'Ghost Vertices Max' $log | awk '{print $(5)}'
echo tot elm
grep 'Total Elements Max' $log | awk '{print $5}'
echo imb elm
grep 'Total Elements Max' $log | awk '{print $(NF)}'
echo ghost elm
grep 'Ghost Elements Max' $log | awk '{print $(5)}'
