#!/bin/bash
#-v: filter out search term
cd /problems/f625672abc185c8d615f852c306d877f
for i in `seq 1 4096`; do
        ./bashloop $i | grep -v "Nope"
        done
