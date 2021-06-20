# Desk WeatherStation with esp8266 and Python-Flask web application

Desk WeatherStation with esp8266, 1,3" oled display, GY-BME280 sensor and Python-Flask web application for data visualization.

![IMG_9997](https://user-images.githubusercontent.com/63566699/122669852-6c3fa080-d1bf-11eb-930a-4914e73b7bcb.jpg)

## Pin Connections
The pin connections are the same as indicated in the KeeYees kit tutorial but I report them below:

NodeMCU ESP8266<------->OLED

3.3V---VCC

GND---GND

D1---SCL

D2---SDA

NodeMCU ESP8266<------->BME280

3.3V---VCC

GND---GND

D1---SCL

D2---SDA


## Esp8266 Code Description
For the project I used this KeeYees kit that can be purchased at this link: https://www.amazon.it/KeeYees-GY-BME280-Atmosferica-Temperatura-Breadboard/dp/B07T2H5QXC/ref=sr_1_12?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=keeyees&qid=1624183225&sr=8-12

The arduino code is the same as provided by the KeeYees demo except for a function that I inserted in the code that allows you to send the bme sensor data to the Python web application. Below the function:

![image](https://user-images.githubusercontent.com/63566699/122677332-36f87a00-d1e2-11eb-9662-7471f9739d6b.png)

N.B. : it would be more correct to make a post call but for ease I made a get.

## Python Web Application Description
The python web application with Flask allows you to view the latest BME sensor data sent by esp8266 and the graphs (with the Plotly library) that show the trend of temperature, humidity and atmospheric pressure over time. The data is saved on the MySQL DB.
I have deployed my application (also the DB) on pythonanywhere.


https://user-images.githubusercontent.com/63566699/122678847-bee18280-d1e8-11eb-972e-68f4b4f80f04.mov




## Demo
https://user-images.githubusercontent.com/63566699/122670651-65b32800-d1c3-11eb-873c-ad8b4ba14d24.MOV


