# read_temp.py

from w1thermsensor import W1ThermSensor

# Inicializa el sensor
sensor = W1ThermSensor()

# Lee la temperatura en grados Celsius
temperature_celsius = sensor.get_temperature()

# Imprime la temperatura
print(f"{temperature_celsius:.2f}")
