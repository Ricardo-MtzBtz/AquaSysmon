# AquaSysmon
Sistema para el monitoreo del agua: Sistema encargado de la recoleccion de datos / valores en tiempo real, para el analisis y graficacion de resultados


PRIMERO PASOS DE INCIO

  #Comando para iniciar con el entorno virtual en la raspberry

python3 -m venv my_env   #Cambia el nombre "my_env" de entorno que vas a crear para que sea mas facil de identificar

  #Comando para activar el entorno virtual 

source my_env/bin/activate  #Cambia el "my_env" por el nombre del entorno que creaste

  #Instalacion de liberias en el entorno virtual que creamos

pip install adafruit-circuitpython-dht Adafruit-Blinka

  #Creacion del codigo para la lectura DTH22

nano dht22.py

  #Comando para dar los permisos necesarios a los scripts para poder ejecutarlos desde cualquier usuario.

chmod +x /home/pi/run_sensor.sh   #Cambia el nombre y el tipo de formato cual sea su caso 


  #Comando que se agrega en los archivos del servidor

UserParameter=temperature.water,/home/pi/run_sensor.sh #cambiar respecto al nombre del script y la ruta en la que se encuentra

