
##Lab 2A: General-purpose input/output (GPIO) and serial communication

Following the instruction, I connected the 4th and the 5th serial pins from the left of the top row. Then I installed and run Minicom, enabled new line and enabled echo. The result is as below.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab2/lab2-1.png)

I didn't do the option step since I don't have two respberry Pi.

##Lab 2B: Serial peripheral interface (SPI)

I connect the SPI COPI and CIPO pins and did a spidev-test. The result is as below.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab2/lab2-2.png)

##Lab 2C: Breadboard

Following the instruction, I connect the LED module to my raspberry Pi.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab2/lab2-4.jpg)

##Lab 2D: Light-emitting diode (LED)

I entered the following commands and successfully switched the LED on and off.
  pi@raspberypi:~ $ sudo su
  root@raspberypi:/home/pi# echo 18 > /sys/class/gpio/export
  root@raspberypi:/home/pi# cd /sys/class/gpio/gpio18
  root@raspberypi:/sys/class/gpio/gpio18# echo out > direction
  root@raspberypi:/sys/class/gpio/gpio18# echo 1 > value
  root@raspberypi:/sys/class/gpio/gpio18# echo 0 > value
  root@raspberypi:/sys/class/gpio/gpio18# cd /home/pi
  root@raspberypi:/home/pi# echo 18 > /sys/class/gpio/unexport
  root@raspberypi:/home/pi# exit

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab2/lab2-4_(1).jpg)

##Lab 2E: Inter-integrated circuit (I2C)

Following the instruction, I connected I2C device ADXL345 to 3V3, GND, SDA, and SCL of my Raspberry Pi.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab2/lab2-5.jpg)

And I ran the code to send an email to my subaccount. My subaccount received the mail successfully.

And I can detected the device by entering the following command.
  sudo i2cdetect -y 1
  
![alt text](https://github.com/wastelander47/629IoT/blob/main/lab2/lab2-3.png)

##Lab 2F: 1-Wire

Since I don't have DS18B20, I used S8550 D331 instead. After the connection, I tried to find it from my raspberry Pi. And as the screenshot shown, the 00-420000000000 and 00-c20000000000 should be that device.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab2/lab2-6.png)

But after the first try, I can't find the file again. Maybe there's something broke in the circuit.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab2/lab2-6_(1).png)
