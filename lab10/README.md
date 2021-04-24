# Lab 10: Blockchain

## Lab 10A: Blockchain

### Hash function with randomization

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-1.png)

### SHA-2 Secure Hash Algorithm

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-2.png)

### Build the tiniest blockchain in less than 50 lines of Python by Gerald Nash 

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-3.png)

### Let’s Make the Tiniest Blockchain Bigger Part 2: With More Lines of Python by Gerald Nash

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-4.png)

### Python blockchain app by Satwik Kansal

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-5.png)

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-6.png)

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-7.png)

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-8.png)

## Lab 10B: IOTA

Following the instruction, I downloaded and built the C library for BCM2835. Then I cloned the code repository and changed nodes.testnet.iota.org to nodes.devnet.iota.org.

Since transactions in the Devnet must use a minimum weight magnitude (MWM) of 9 to be valid, I edited mam.client.js with ^W to search mwm and changed it from 14 to 9 at the end of Line 23375.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-9.png)

After that I ran mam_publish.js at Terminal 1 and ran mam_receive.js at Terminal 2.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-10.png)

Since I don't have DHT22, I used DHT11 again but changed GPIO pin from 4 to 24.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-circuit.png)

After that I ran mam_sensor.js at Terminal 1 and ran mam_receive.js at Terminal 2.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab10/lab10-11.png)


