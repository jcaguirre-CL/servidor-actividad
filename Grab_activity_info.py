#!/usr/bin/env python
# coding: utf-8
# In[1]:
import xml.etree.ElementTree as ET
import sys
import re
from pymongo import MongoClient

filename = sys.argv[1]
tree = ET.parse(filename)
root = tree.getroot()
#directory = '06-03-20 01'
#date = '06-03-20 010034 1101'
#'06-03-20 010034 1101.xml'
#s = "abc123AUG|GAC|UGAasdfg789"
#pattern = "AUG\|(.*?)\|UGA"
#./IN/Ejemplo_from_PISIS.xml
#pattern = "LOCAL\/(.*?)\/(.*?)\.xml"
pattern = "LOCAL\/(.*?)\.xml"
print (filename)
date = re.search(pattern, filename).group(1)

month = date[0:2]
day = date[3:5]
year = date[6:8]
hour = date[8:10]
minute = date[10:12]
print ("Creando registro: ", filename, day, month, year, hour, minute)
# In[3]:
client = MongoClient('localhost', 27017)
db = client['activity-server']
collection = db['collection']
# In[4]:
registros = db.registros
# In[5]:
for yuhuuu in root.iter('clientBandwidth'):
    tipo = "Editora" if "edi" in yuhuuu[2].text else yuhuuu[2].text[3:6]
    if round(float(yuhuuu[0].text))!=0 or round(float(yuhuuu[1].text))!=0:
        actividad = hour+':'+minute
        contador = yuhuuu[2].text
        print (contador)
    else: 
        actividad = ""
        contador = ""
    registro = {
        "dia": day,
        "mes": month,
        "anio": '20'+year,
        "hora": hour+':'+minute,
        #"hora": str(int(hour) - 1)+':'+minute,
        #"minuto": minute,
        "Servidor": 'PISIS',
	"Equipo": yuhuuu[2].text,
        "Lectura": round(float(yuhuuu[0].text)),
        "Escritura": round(float(yuhuuu[1].text)),
	"Actividad": actividad,
        "Contador": contador,
        "Tipo": tipo,
    }
    registro_id = registros.insert_one(registro).inserted_id
    #print("Read: ",round(float(movie[0].text)))    
    #print("Write: ",round(float(movie[1].text)))
    #print("Name: ",movie[2].text)
# In[ ]:




