## Lab 5A: Crossbar.io

Following the instruction,　I installed Docker on Raspberry Pi OS. Ran cURL to download data from example.com with the progress meter.
, ran Docker commands and hello-world and added pi to the Docker group as a non-root user, logout SSH, and reconnect SSH for this to take effect.

Then I ran Crossbar.io router on Terminal 1 and got the Crossbar.io node information on 127.0.0.1:8080/info via VNC Viewer.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab5/lab5-1.png)

After that I ran publish-client on Terminal 2 and ran subscribe-client on Terminal 3 so that I can get the data from Terminal 3 to Terminal 2.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab5/lab5-2.png)

## Lab 5B: Eclipse Mosquitto and Eclipse Paho

Following the instruction, I installed and ran Mosquitto to subscribe on Terminal 1 and publish on Terminal 2.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab5/lab5-3.png)

Then I installed Paho and ran code to subscribe on Terminal 1 and publish on Terminal 2.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab5/lab5-4.png)

And this is the multiple version.
![alt text](https://github.com/wastelander47/629IoT/blob/main/lab5/lab5-5.png)

At last I copied system_info.py, subraspi.py, pubraspi.py from ~/iot/lesson5 to ~/demo

Replace topic "Raspberry Pi" with "Tianze" in both subraspi.py and pubraspi.py

And ran subraspi.py on Terminal 1 and pubraspi.py on Terminal 2

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab5/lab5-5.png)
