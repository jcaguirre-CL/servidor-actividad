#!/bin/bash
cd /root/actividad/activity
mongoexport --db activity-server --collection registros --type=csv --fields dia,mes,anio,hora,minuto,Servidor,Equipo,Lectura,Escritura,Actividad,Contador,Tipo --out ./ACTIVIDAD.csv
if [ -f ./ACTIVIDAD.csv ]; then
   #count=`wc -l ./MCRV1-2020.csv`
   #eco $count | awk '{print $1}'o "$count = ${!count}"
   #python depurar.py "./MCRV1-2020.csv" "./MCRV1-2020.xlsx" "MCRV1-2020" "./MCRV2-2020.xlsx" `echo $count | awk '{print $1}'`
   #python depurar.py "./MCRV1.csv" "./MCRV1.xlsx" "MCRV1" "./MCR-INFORME-FULL.xlsx" `grep 000Z MCRV1.csv | wc -l`
  # while read p; do
     #sed -i 's/,/,,,/g' $p
   #  echo "$p"
  # done <./MCRV1-2020.csv
   #cp ./MCR-INFORME-FULL.xlsx "INFORME-MCR-$(date +"%m-%d-%y").xlsx"
   #rclone copy "INFORME-MCR-$(date +"%m-%d-%y").xlsx" remote:FOLDER
   #python3 depurar.py
   rclone copy ./ACTIVIDAD.csv remote:FOLDER
   echo 'ARCHIVO OK'
   echo "$(date)"
   #rm -rf MCR*
#   rm -rf INFORME*
fi
