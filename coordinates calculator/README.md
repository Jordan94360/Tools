<img src="https://static1.makeuseofimages.com/wordpress/wp-content/uploads/2016/02/measure-google-maps.jpg">

# **Latitude/Longitiude Calculator: Measuring lists of plots against each other** #

## **1. Description** ##
 A program that compares a list of coordinates against another list of coordinates and calculates the distance between them. The coordinate pair with the shortest distance are returned to a dataframe.


### *Background:* ###
 I had a list of coordinates for different key locations and a seperate list of coordinates for events and I wanted to see which of the events was the closest to any of my locations without mannually entering each one into Google Maps or another mapping application. 

## **2. Prequisites** ##
- [Python 3](https://www.python.org/)
- [Haversine library](https://pypi.org/project/haversine/)

***
## **3. Usage** ##


- **3.1** Provide two seperate .csv files each containing two columns labled "Lat" and "Long" with the respective coordinate data. See below for example. The program will lable the two files *list_1* and *list_2*.

<img  src="https://raw.githubusercontent.com/Jordan94360/Tools/main/coordinates%20calculator/images/lat_long_data_example.png" width="280" height="260" >

<p>&nbsp;<p>

- **3.2** Once ran, a dataframe labled "closest_location" will be created, it will contain the final results of the program. The first column contains the calcuated distance between the two closest coordinates (in miles by default). The second and third columns contain the two coordinate pairs.

<img src="https://github.com/Jordan94360/Tools/blob/main/coordinates%20calculator/images/output_example.png?raw=true"
width="600" height="600">


- 3.3 The distance units can be changed by altering the *unit* variable based on the [haversine documentation](https://pypi.org/project/haversine/)

***

## **4. How it Works** ##
<img src="https://github.com/Jordan94360/Tools/blob/main/coordinates%20calculator/images/workflow.png?raw=true">

***

