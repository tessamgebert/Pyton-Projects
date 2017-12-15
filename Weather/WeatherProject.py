"""
Weather Project for Python 
By: Tessa Gebert
"""

import sys
print sys.argv[1]
file_name = sys.argv[1]
weather = open(file_name, "r")
a = weather.readline() 
lista = a.split(",")
i = 0
tmax = 0
tmin = 0
awnd = 0
prcp = 0
date = 0
for header in lista:
    if header == "TMAX":
        tmax = i
    if header == "TMIN":
        tmin = i
    if header == "AWND":
        awnd = i
    if header == "PRCP":
        prcp = i
    if header == "DATE":
        date = i
    i += 1

position = [tmax, tmin, awnd, prcp, date]
max_temp = []
min_temp = []
wind_speed = []
rain = []
dates = []
differences = []
for row in weather:
    weather_row = row.split(",")
    max_temp.append(float(weather_row[position[0]]))
    min_temp.append(float(weather_row[position[1]]))
    wind_speed.append(float(weather_row[position[2]]))
    rain.append(float(weather_row[position[3]]))
    dates.append(int(weather_row[position[4]]))
    x = (float(weather_row[position[0]]))
    y = (float(weather_row[position[1]]))
    differences.append(x - y)
# This adds all the values in the same position as each of the headers.
 
value = 0
c = 0 
total_speed = 0
for value in wind_speed:
    total_speed += value/10
    c += 1

average_speed = total_speed/c
high_temp = max(max_temp)
min_delta = min(differences)
total_rain = 0
for value in rain:
    total_rain += value

iteration = 0
temp_dates_index = []
for value in max_temp:
    if value == high_temp:
        temp_dates_index.append(iteration)
    iteration += 1

min_date = []
for indexes in temp_dates_index:
    min_date.append(dates[indexes])

early_date = min(min_date)	
iteration = 0
index = 0
for value in differences:
    if value == min_delta:
        index = iteration
    iteration += 1

early_date = str(early_date)
day = str(dates[index])
early_date = early_date[4:6] + "/" + early_date[6:8] + "/" + early_date[0:4]
day = day[4:6]+"/" + day[6:8] + "/" + day[0:4]
high_temp = high_temp/10
f_convert_max = high_temp*1.8 + 32
min_delta = min_delta/10
f_convert_dif = min_delta*1.8
round_wind_speed = round(average_speed, 2)
print "File to be analyzed (.csv only): " + sys.argv[1]
print "Maximum temperature (F): " + str(f_convert_max) + " on " + early_date
print "Minimum temperature difference (F): " + str(f_convert_dif) + " on " + day
print "Average wind speed (m/s): " + str(round_wind_speed)
print "Total precipitation (mm): " + str(total_rain)   
