#! /bin/bash


# check if argument is given # must be a correct file path
if [ $# -eq 1 ]; then

# put all the mimetype into an array
all_mimetype=`cat $1 | awk '{print $4}' | sort | uniq`

number_of_mimetype=`echo $all_mimetype | wc -w`

#echo "$all_mimetype"
for x in $all_mimetype; do
    echo -n "$x total=";
    temp=`cat $1 | grep $x`
# FOR each mimetype # check awk $4 (the mimetype column) if equal current mimetype then proceed
    echo "$temp" | wc -l|tr -d '\n'|tr -d ' '; echo -n ": ";
#  for all of these line  // output the extension of the file
#   find the extension
#   sed "s/.*\.\(.*\)/\1/g"
#  proceed all of those extensions to have their numbers
    echo -n "$temp" | awk '{print $1}'|sed "s/.*\.\(.*\)/\1/g" | sort | uniq -c | xargs;
# then print the mimetype: the number of them: all the extension + their numbers


done






#obsolete temp commmand
# a="https:__www.og.berr.gov.uk_upstream_field_development_2009ReservesMetric.xls"; len=`echo $a | wc -c`; echo $a | cut -c $(($len-4 ))-$(($len))
#cat xls_csv_1.cdx | awk '{print $4}' | sort | uniq -c > stat/mimetype_last_stats
#
#
#cat xls_csv_1.cdx | awk '{print $1}' | while read a; do
#echo $a | sed "s/.*\.\(.*\)/\1/g"
#done | sort | uniq -c > from_file_log
fi
