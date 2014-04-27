#!/bin/bash
project=$1
if [ -z $project ]; then echo "Usage: start-project.sh projectname"; exit; fi

filedir=$(pwd)
xml_file=${filedir}/looper.xml
project_file=${filedir}/${project}.als

cp ${xml_file} ${project_file}

echo "Launching project: ${project_file}"
open ${project_file}

