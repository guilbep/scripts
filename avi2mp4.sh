#! /bin/bash
echo "Enter filename in current directory:"
read VID
if [ -f $VID ]
    then
    echo "Found ${VID}... Starting ffmpeg."
    ffmpeg -i $VID -threads 4 -acodec libfaac -b:a 128k -vcodec mpeg4 -b:v 1200k -flags +aic+mv4 `basename $VID avi`'mp4'
    else
    echo "Not a file, exiting..."
fi
