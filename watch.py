#!/usr/bin/env python
#import smtplib
import re
import datetime
import fcntl
import signal
import os
import shutil
import sys
import time
import logging
import subprocess
#import telegram
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import FileSystemEventHandler
from sys import platform as system_platform
from array import *

class JcHandler(FileSystemEventHandler):
    def __init__(self, observer):
        self.observer = observer

    def on_created(self, event):
        time.sleep(2)
        nombre = event.src_path
        print (nombre)
        nombre = nombre.replace("IN-LOCAL", "LOCAL")
        print ("path completo: ",nombre)
        #pattern = "LOCAL\/(.*?)\/"
        #directorio = re.search(pattern, nombre).group(1)
        #directorio = directorio.replace(" ", "")
        #print ("directorio: ",directorio)
        #subprocess.call(['mkdir','LOCAL/'+directorio])
        nombre = nombre.replace(" ", "")
        print ("path sin espacios: ",nombre)
        if not nombre == event.src_path:
            subprocess.call(['cp',event.src_path,nombre])
            logging.info('Eliminando espacios!!')
        #print nombre
        logging.info('Working on: %s', nombre)
        print ("Working on:", nombre)
        proc = subprocess.Popen(["./ejecutar.sh", nombre])
        logging.info('Proc ID WEB : %s', proc)
        pc = proc.communicate()[0]
        pc1 = proc.communicate()[1]
        logging.info('pc1 : %s', pc1)
        #print pc
        rc = proc.returncode
        if not rc:
            print ("Proceso OK")
            logging.info('OK')
        else:
            print ("Proceso Failed")
            logging.warning('Failed')


if __name__ == "__main__":
    logfile = './proceso.log'
    print ("Observando directorio!!!")
    logging.basicConfig(filename=logfile,level=logging.DEBUG,format='%(asctime)s :: %(levelname)s ::: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('Observando directorio!!!')
    path = "./IN-LOCAL"
    observer = Observer()
    event_handler = JcHandler(observer)
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
