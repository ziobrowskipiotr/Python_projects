import random
from math import radians, sin, cos, sqrt, asin
import math
import time
cities=[]
with open('TSP.txt', 'r') as file:
    for line in file:
        city, latitude, longitude = line.split()
        cities.append([int(city), float(latitude), float(longitude)])

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    d = R * c
    return d

def changing(list):
    temp_list = list[1:]
    random.shuffle(temp_list)
    list[1:] = temp_list
    return list
def nearest_neighbour(list):
    if len(list) <= 1:
        return list
    distance = 2 * float(math.pi) * 6378
    for j in range(1, len(list)):
        if haversine(list[0][1], list[0][2], list[j][1], list[j][2]) < distance:
            distance = haversine(list[0][1], list[0][2], list[j][1], list[j][2])
            d = j
    list[1], list[d] = list[d], list[1]
    new_list = [list[0]] + nearest_neighbour(list[1:])
    return new_list
def distance(list):
    list.append(list[0])
    result = []
    for i in range(len(list)-1):
        result.append(float(haversine(list[i][1], list[i][2], list[i+1][1], list[i+1][2])))
        print("Route", i+1, "(city", list[i][0], "to city", list[i+1][0], "), distance:", result[i], "kilometers")
    print("All distance:", sum(result))

start_time = time.time()
cities = changing(cities)
cities = nearest_neighbour(cities)
distance(cities)
print("Time: %s seconds" % (time.time() - start_time))