

```python
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from citipy import citipy
import openweathermapy as ow

from config import api_key

```


```python
                                                    #PSEUDOCODE

#create an array of cities based on lat and long
    #generate random coordnates - check
    #use citipy to generate nearest city - check
        #make sure cities are unique
#loop through array
    #in the loop, make an api call to each city and append data to a list:
    #put weather data - lat, temp, humidity, clouds, wind speed into separate lists
#create dataframe with weather data and city name
#plot data from dataframe
```


```python
#create an array of cities based on lat and long
    #generate random coordnates - check
coord = []
tup = ()
for limit in range(1000):
    lat, long = np.random.uniform(-180,180), np.random.uniform(-90, 90)
    tup = (lat,long)
    coord.append(tup)

```


```python
#use citipy to generate nearest city - check
empty = []
for i in range(0,len(coord)):
    city = citipy.nearest_city(coord[i][0], coord[i][1])
    empty.append(city.city_name)

#Make sure cities are unique    
city_list = []
for j in empty:
    if j not in city_list:
        city_list.append(j)
    else:
        city = citipy.nearest_city(np.random.uniform(-180,180), np.random.uniform(-90, 90))
        city_new = city.city_name
        empty.append(city_new)
                  
#Check if cities are unique:
city_set = set(empty)
if len(city_set) == len(city_list):
    print("Cities are unique")

```

    Cities are unique
    


```python
#Do the api call:
settings = {"units": "metric", "appid": api_key}
weather_data = []
not_found = []

#Loop through the city list and catch for 404 errors for cities that don't have weather data
for city in city_list:
    if len(weather_data) > 700:
        break
    else:
        try:
            weather_data.append([ow.get_current(city, **settings)])        
        except Exception as err:
            not_found.append(city)
            continue
print("The following cities could not be found: \n")
print(not_found)
```

    The following cities could not be found: 
    
    ['bengkulu', 'barentsburg', 'illoqqortoormiut', 'karaul', 'belushya guba', 'warqla', 'taolanaro', 'berbera', 'bantry', 'urumqi', 'amderma', 'mouzakion', 'tsihombe', 'taltal', 'solovetskiy', 'marcona', 'louisbourg', 'attawapiskat', 'koyilandi', 'olafsvik', 'tumannyy', 'kosya', 'grand river south east', 'korla', 'barawe', 'kachikau', 'kemijarvi', 'chissamba', 'tres lagoas', 'saint quentin', 'zhovtneve', 'balykshi', 'chigorodo', 'vedaranniyam', 'kytlym', 'aflu', 'labrea', 'maarianhamina', 'longlac', 'polikastron', 'kalavrita', 'zachagansk', 'tunduru', 'ciras', 'vicuna', 'kashi', 'achisay', 'bur gabo', 'zmiyiv', 'toliary', 'formoso do araguaia', 'leghorn', 'borama', 'machali', 'acarau', 'raga', 'santa eulalia del rio', 'rolim de moura', 'el reten', 'khokholskiy', 'el faiyum', 'bossembele', 'aberystwyth', 'westpunt', 'irbil', 'umzimvubu', 'doctor pedro p. pena', 'stornoway', 'krasnoselkup', 'araguacu', 'ipora', 'rudbar', 'tsienyane', 'varzea alegre', 'sitio novo do tocantins', 'malwan', 'andenes', 'talah', 'bolshoy tsaryn', 'bargal', 'saryshagan', 'tambopata', 'mahaicony', 'mwaya', 'kargil', 'burica', 'sento se', 'yakshur-bodya', 'hunza', 'vestbygda', 'fianga', 'tome-acu', 'tingrela']
    


```python
#Create Dataframe to hold Weather Data:
data_list = []
names = []
for item in weather_data:
    for response in item:
        data = ( response['main']['temp'], response['main']['humidity'], response['wind']['speed'],
            response['clouds']['all'],  response['coord']['lat'],    response['coord']['lon']) 
        name = (response['name'])
        names.append(name)
        data_list.append(data)


#put weather data - lat, temp, humidity, clouds, wind speed into separate lists
weather_data_df = pd.DataFrame(data_list)
column_names = ["Temp","Humidity","Wind Speed","Cloudiness(%)", "Latitude", "Longitude"]
weather_data_df = pd.DataFrame(data_list, index = names , columns=column_names)

```


```python
x = weather_data_df['Latitude']
weather_data_df.to_csv('Weather_Data.csv')
weather_data_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Temp</th>
      <th>Humidity</th>
      <th>Wind Speed</th>
      <th>Cloudiness(%)</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Narsaq</th>
      <td>-7.00</td>
      <td>44</td>
      <td>3.10</td>
      <td>0</td>
      <td>60.91</td>
      <td>-46.05</td>
    </tr>
    <tr>
      <th>Ipixuna</th>
      <td>22.00</td>
      <td>94</td>
      <td>3.10</td>
      <td>75</td>
      <td>-1.76</td>
      <td>-48.80</td>
    </tr>
    <tr>
      <th>Njombe</th>
      <td>16.20</td>
      <td>99</td>
      <td>0.88</td>
      <td>80</td>
      <td>-9.34</td>
      <td>34.77</td>
    </tr>
    <tr>
      <th>Qandala</th>
      <td>13.80</td>
      <td>100</td>
      <td>0.43</td>
      <td>8</td>
      <td>11.47</td>
      <td>49.87</td>
    </tr>
    <tr>
      <th>Bredasdorp</th>
      <td>17.00</td>
      <td>88</td>
      <td>3.10</td>
      <td>92</td>
      <td>-34.53</td>
      <td>20.04</td>
    </tr>
    <tr>
      <th>Tasiilaq</th>
      <td>-9.00</td>
      <td>43</td>
      <td>1.00</td>
      <td>12</td>
      <td>65.61</td>
      <td>-37.64</td>
    </tr>
    <tr>
      <th>Shelburne</th>
      <td>-4.01</td>
      <td>73</td>
      <td>2.60</td>
      <td>1</td>
      <td>44.08</td>
      <td>-80.20</td>
    </tr>
    <tr>
      <th>Qaanaaq</th>
      <td>-23.56</td>
      <td>100</td>
      <td>0.43</td>
      <td>36</td>
      <td>77.48</td>
      <td>-69.36</td>
    </tr>
    <tr>
      <th>Dikson</th>
      <td>-21.31</td>
      <td>100</td>
      <td>12.78</td>
      <td>48</td>
      <td>73.51</td>
      <td>80.55</td>
    </tr>
    <tr>
      <th>Ushuaia</th>
      <td>6.00</td>
      <td>75</td>
      <td>5.70</td>
      <td>40</td>
      <td>-54.81</td>
      <td>-68.31</td>
    </tr>
  </tbody>
</table>
</div>




```python
#TEMP VS LAT
y_t = weather_data_df["Temp"]
plt.plot(x,y_t,'mo')
plt.xlabel("Latitude")
plt.ylabel("Temp(C)")
plt.title("Temp(C) vs Lat")
plt.grid()
plt.savefig("Temp vs Lat")
plt.show()
```


![png](output_7_0.png)



```python
#HUMIDITY VS LAT
y_h = weather_data_df["Humidity"]
plt.plot(x,y_h,'bo')
plt.xlabel("Latitude")
plt.ylabel("Humidity(%)")
plt.title("Humidity(%) vs Lat")
plt.grid()
plt.savefig("Humidity vs Lat")
plt.show()
```


![png](output_8_0.png)



```python
#WIND SPEED VS LAT
y_ws = weather_data_df["Wind Speed"]
plt.plot(x,y_ws,'ro')
plt.xlabel("Latitude")
plt.ylabel("Wind Speed(mph)")
plt.title("Wind Speed(mph) vs Lat")
plt.grid()
plt.savefig("Wind Speed vs Lat")
plt.show()
```


![png](output_9_0.png)



```python
#CLOUDINESS VS LAT
y_c = weather_data_df["Cloudiness(%)"]
plt.plot(x,y_c,'go')
plt.xlabel("Latitude")
plt.ylabel("Cloudiness(%)")
plt.title("Cloudiness(%) vs Lat")
plt.grid()
plt.savefig("Cloudiness vs Lat")
plt.show()
```


![png](output_10_0.png)

