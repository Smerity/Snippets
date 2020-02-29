#!/bin/bash

rm TIME

for idx in {1..18} # 512}
do
  #./main $(($idx * 128)) >> TIME
  N=$(echo "2 ^ $idx" | bc)
  ./main $N >> TIME
done
