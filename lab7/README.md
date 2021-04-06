## Lab 7A: ThingSpeak

Following the instruction,　I logged in the ThingSpeak, created new channel cpu_loop with field1 cpu_pc and field2 mem_avail_mb, and ran thingspeak_feed.py with my write API KEY.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab7/lab7-1.png)

## Lab 7B: Google Sheets

Following the instruction, I created an rpidata project in the Google Cloud Platform Identity and Access Management.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab7/lab7-2.png)

Then I installed gspread and oauth2client. After that I started a new spreadsheet on Google Sheets. I shared the spreadsheet with the "client_email" address in my .json key file.
After that I changed the address and name shown in rpi_spreadsheet.py and ran it.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab7/lab7-3.png)

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab7/lab7-4.png)

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab7/lab7-5.png)


