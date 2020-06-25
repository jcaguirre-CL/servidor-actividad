#!/bin/bash

nombre=$1

echo "From ejecutar: " $nombre

python3 Grab_activity_info.py $nombre
