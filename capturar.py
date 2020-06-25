import os
import time
import subprocess

path = "./IN"
pathIN = "./IN-LOCAL" #TMP ANTES DE PROCESAR
pathLOCAL = "./LOCAL" #ARCHIVE DE JOBS REALIZADOS
while True:
	# RECUPERAR FILES NO PROCESADOS EN JOB PREVIO
	filesProcesados=[]
	filesCopiados=[]
	filesCopiadosPre=[]
	paraBorrar=[]
	#filesCopiadosPre.append([(z) for x,y,z in os.walk(pathIN)])
	#filesCopiados.append([(z.replace(" ","")) for z in filesCopiadosPre])

	for root,d_names,f_names in os.walk(pathLOCAL):
        	for files in f_names:
                	filesProcesados.append(files.replace(" ","")) #PROCESADOS

	for root,d_names,f_names in os.walk(pathIN):
		for files in f_names:
			if files.replace(" ","") not in filesProcesados:
				paraBorrar.append(files) #NO PROCESADO

	#print (paraBorrar)
	for files in paraBorrar:
		print("archivo borrado: ", pathIN+'/'+files)
		os.remove(pathIN+'/'+files)
	print ("---------LIMPIO--------")
	#time.sleep(10)

	# CAPTURAR NUEVOS FILES EN HISTORY
	for root,d_names,f_names in os.walk(path):
		for files in f_names:
			mystr=root+'/'+files
			#print ("Full path: ",mystr)
			#print ("File: ",mystr[17:])
			if mystr[17:].replace(" ","") not in filesProcesados: 
				print("archivo nuevo...procesar solo minuto 1 3 6 9")
				if files[12:13] in "1369":
					print("Procesando: ",files)
					subprocess.call(['cp',mystr,'./IN-LOCAL']) # IN -> IN-LOCAL
					time.sleep(2)
					print ("------------------------------------------------------------------")
	time.sleep(300)
