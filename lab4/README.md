## Labs 4A and 4B: Django and Django REST

Following the instruction, I installed Django and Django REST framework, then installed MariaDB server and client.

Then I started Django Project "Stevens".

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-1.png)

I created MySQL database and edited settings.py.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-2.png)

After all the steps to setup the app, I enabled Google Maps API and add it into the index.html.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/APIKEY.png)

Then I copied static files from lesson4 to myapp dir, set up the superuser, and ran Django server.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-3.png)
![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-5.png)

After the Django project stevens, I tried Django REST project myraspi.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-4.png)

Similarly to Django app, I setup all the needed. But when I stepped into 

  ~/myraspi $ python3 manage.py makemigrations myapp

There's an error occured and I don't know what's going on. So I stopped here.

## Lab 4C: Flask

Following the instruction, I ran Flask server and open a Chromium browser via VNC Viewer and went to http://127.0.0.1:5000/.
Then I got a Hello World! from hello_world.py.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-10.png)
![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-6.png)

Then I installed Flask-Ask and Ngrok for Alexa Skill Kit (ASK).

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-7.png)

And started memory_game.py.

After that I signed in Alexa Developer Console and created a Hello World Template Skill.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-8.png)

However, when I got to the Interaction Model step, I didn't know where I should replace with iot/lesson4/memory_game.json. So I stopped Lab4C there.

![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-9.png)

## Lab 4D: LAMP

Following the instruction, I installed Apache HTTP server and PHP.

However, there's no /var/www/html file on my raspberry Pi. So I stopped Lab 4D there. 


![alt text](https://github.com/wastelander47/629IoT/blob/main/lab4/lab4-11.png)

I'll tried to contact to professor to ask the above 3 problems I met.
