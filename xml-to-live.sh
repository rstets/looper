#!/bin/bash

filepath=$1
if [ -z $filepath ]; then echo "Usage: xml-to-live.sh projectfile.xml"; exit; fi


filedir=$(dirname $filepath)
filename=${filepath%.*}
gz_file=${filepath}.gz
als_file=${filedir}/${filename}.als

gzip -k $filepath
mv -f ${gz_file} ${als_file}
echo "Converted ${filepath} to ${als_file}"
echo ""

