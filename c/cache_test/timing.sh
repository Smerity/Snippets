#!/bin/bash

rm TIME

#for idx in {9..18}
for idx in {1..128}
do
  N=$(($idx * 128))
  #N=$(echo "2 ^ $idx" | bc)
  ./main $N >> TIME
done
