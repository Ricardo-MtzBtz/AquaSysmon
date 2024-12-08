from w1thermsensor import W1ThermSensor

# Inicializa el sensor
sensor = W1ThermSensor()

# Lee la temperatura en grados Celsius y Fahrenheit
temperature_celsius = sensor.get_temperature()
temperature_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)

# Imprime las temperaturas
print(f"{temperature_celsius:.2f} °C")
print(f"{temperature_fahrenheit:.2f} °F")
