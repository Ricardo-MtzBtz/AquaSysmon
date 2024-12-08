#!/bin/bash

# Activa el entorno virtual 
source /home/pi/sys/bin/activate   #Cambiar la ruta dependiendo de la direccion de la carpeta donde se instalo el entorno virtual      

# Ejecuta el script de Python que lee la temperatura  
python /home/pi/read_temp.py  #Cambaiar ruta en donde esta almacenada el archivo python 

# Desactiva el entorno virtual
deactivate
