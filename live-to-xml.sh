#!/bin/bash

filepath=$1
if [ -z $filepath ]; then echo "Usage: live-to-xml.sh projectfile.als"; exit; fi


filedir=$(dirname $filepath)
filename=${filepath%.*}
xml_file=${filedir}/${filename}.xml
gz_file=${xml_file}.gz

cp -f ${filepath} ${gz_file}
gunzip ${gz_file}
echo "Converted ${filepath} to ${xml_file}"
echo ""


