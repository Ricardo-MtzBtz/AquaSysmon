import time
import adafruit_dht
import board

# Configura el pin de datos del sensor DHT22 (usa el GPIO correcto)
dht_device = adafruit_dht.DHT22(board.D4)

while True:
    try:
        # Lee temperatura y humedad
        temperature = dht_device.temperature
        humidity = dht_device.humidity

        print(f"Temp: {temperature:.1f} °C    Humidity: {humidity:.1f}%")
    except RuntimeError as e:
        # Maneja errores comunes del sensor
        print(f"Error: {e.args[0]}")
    time.sleep(2.0)
