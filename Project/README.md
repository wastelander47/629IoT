
# Room Temperature and Humidity Monitor

## Introduction
In this project I implemented a room temperature and humidity monitor via Raspberry Pi 4. The DHT11 sensor was used to monitor the room's temperature and humidity and the flask was used to upload the result to the website. The project was implemented by python3.


## DHT11 
The DHT11 temperature and humidity sensor is a nice little sensor that provides digital temperature and humidity readings. It’s really easy to set up, and only requires one wire for the data signal. These sensors are popular for use in remote weather stations, soil monitors, and home automation systems.

In this project, the DHT11's VCC is connected with 3.3V on Raspberry Pi. The DATA is connected with BCM24. The GND is connected with GND.

![alt text](https://github.com/wastelander47/629IoT/blob/main/Project/connection.jpg)

## Flask
Flask is a web framework. This means flask provides you with tools, libraries and technologies that allow you to build a web application. This web application can be some web pages, a blog, a wiki or go as big as a web-based calendar application or a commercial website.

In this project, flask is used to upload the result getting from DHT11 and upload it to the website.

## Implementation
First of all, I connected the DHT11 sensor with my Raspberry Pi. Then I implemented a method called get_dht_data() to get the temperature and humidity from the sensor. This method can not only get the Celsius temperature and humidity but also calculate the Fahrenheit temperature. The method returns the Celsius temperature, the Fahrenheit temperature_f, and the humidity.

After that, I built a string to save the temperature and humidity and implemented the flask part to upload the string to the local host 127.0.0.1:5000. The screenshot of the webpage and the backend are shown below.
```linux
python3 DHT11.py
```

![alt text](https://github.com/wastelander47/629IoT/blob/main/Project/local_url.png)

![alt text](https://github.com/wastelander47/629IoT/blob/main/Project/backend.png)

Then for the remote display, I changed the address to my Raspberry Pi's IP address and ran the code again.

![alt text](https://github.com/wastelander47/629IoT/blob/main/Project/remote_url.png)

![alt text](https://github.com/wastelander47/629IoT/blob/main/Project/backend2.png)

The code always uploads the latest data read from DHT11. Refresh the web page to get the latest data.
![alt text](https://github.com/wastelander47/629IoT/blob/main/Project/remote_url2.png)

By accessing the Raspberry Pi's IP address with the pre-set port, users can get the temperature and humidity information of their room anytime and anywhere.
