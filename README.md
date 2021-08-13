![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)

<p align="center">
  <img alt="logo" src="https://user-images.githubusercontent.com/63566699/129363483-482f40ab-d79a-4840-8403-ea86b529e504.png">
</p>

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


![weatherStation_schematics vpd](https://user-images.githubusercontent.com/63566699/124649145-6a046400-de98-11eb-9ae6-82c244e2d203.jpg)



## Esp8266 Code Description
For the project I used this KeeYees kit that can be purchased at this link: https://www.amazon.it/KeeYees-GY-BME280-Atmosferica-Temperatura-Breadboard/dp/B07T2H5QXC/ref=sr_1_12?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=keeyees&qid=1624183225&sr=8-12

I also used the terminal adapter for esp8266: https://www.amazon.it/KeeYees-Espansione-ESP8266-ESP-12E-Sviluppo/dp/B08HYZ4Y69/ref=sr_1_5?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=scheda+di+espansione+esp8266&qid=1625037621&sr=8-5

The arduino code is the same as provided by the KeeYees demo except for a function that I inserted in the code that allows you to send the bme sensor data to the Python web application. Below the function:

![image](https://user-images.githubusercontent.com/63566699/122677332-36f87a00-d1e2-11eb-9662-7471f9739d6b.png)

N.B. : it would be more correct to make a post call but for ease I made a get.

## Python Web Application Description
The python web application with Flask allows you to view the latest BME sensor data sent by esp8266 and the graphs (with the Plotly library) that show the trend of temperature, humidity and atmospheric pressure over time. The data is saved on the MySQL DB.
I have deployed my application (also the DB) on pythonanywhere.


https://user-images.githubusercontent.com/63566699/122678847-bee18280-d1e8-11eb-972e-68f4b4f80f04.mov




## Demo
https://user-images.githubusercontent.com/63566699/122670651-65b32800-d1c3-11eb-873c-ad8b4ba14d24.MOV

## How to change the logo shown on the display

To change the logo to be shown on the display follow the steps:
1.  choose a logo without shading
2.  change the resolution to adapt it to the size of the display (I chose 79x31 in order to view the footer with temperatures and time on the display). You can       change the resolution with Paint
3.  Convert the logo from png or jpeg to xbm using online tools
4.  Finally replace the xbm code generated in WeatherStationImages.h in logo PROGMEM

![image](https://user-images.githubusercontent.com/63566699/122680036-b5a6e480-d1ed-11eb-9f09-a96ce5628539.png)

![IMG_0002](https://user-images.githubusercontent.com/63566699/122680078-eb4bcd80-d1ed-11eb-9c66-81f6451eabd0.jpg)

## To Do

:heavy_check_mark: collapsable area for latest weather data

:x: add logging on DB

:x: view system logs in another collapsible area

:heavy_check_mark: add symbols indicating whether the system is working or not:

![image](https://user-images.githubusercontent.com/63566699/125974641-41e2e72a-04b7-4d77-a63a-d4274c708ce6.png)


## License


[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


License: [MIT](https://github.com/albino98/Arduino_Desk_Weatherstation/blob/main/LICENSE)
