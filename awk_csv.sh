#! /bin/sh

cat ~/Downloads/*.csv | awk 'BEGIN{FS=","}!n{n=NF}n!=NF{failed=1;exit}END{exit !failed}'