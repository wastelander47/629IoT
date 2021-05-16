# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
#dhtDevice = adafruit_dht.DHT22(board.D18)
#dhtDevice = Adafruit_DHT.DHT11(board.D24)
dhtDevice = adafruit_dht.DHT11(board.D24)

from flask import Flask
from flask import send_from_directory
import os
app = Flask(__name__)
temp = ""

def get_dht_data():
    while True:
        try:
            temperature = dhtDevice.temperature
            temperature_f = temperature * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(temperature, humidity)
            if temperature is not None and humidity is not None:
                return temperature, temperature_f, humidity
            else:
                raise
        except:
            time.sleep(0.5)

@app.route("/")
def status():
    temperature, temperature_f, humidity = get_dht_data()
    temp = "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature, humidity)
    print(temp)
    return temp


if __name__ == "__main__":
    allowed_ip_addr = "192.168.86.55"
    #allowed_ip_addr = "127.0.0.1"
    app.run(host=allowed_ip_addr, port=5000, debug=True, threaded=True, use_reloader=False)

