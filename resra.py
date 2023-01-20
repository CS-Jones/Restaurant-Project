from pprint import pprint
import time 
import os
import googlemaps 
import pandas as pd
import json

API_KEY = open('API_KEY.txt').read() 
map_client = googlemaps.Client(API_KEY)

new_places = {}
newnew = {}


def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0
        
        
address = ''
geocode = map_client.geocode(address=address)
(lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))        

search_type = 'restaurant'
distance = miles_to_meters(1000)
restaurant_list= []

response = map_client.places_nearby(
    location=(lat, lng),
    type = search_type,
    radius=distance
)

restaurant_list.extend(response.get('results'))
next_page_token = response.get('next_page_token')

while next_page_token:
    time.sleep(2)
    response = map_client.places_nearby(
        location=(lat, lng),
        keyword=search_type,
        radius=distance,
        page_token=next_page_token
        
    )   
    restaurant_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')    
    

for place in response['results']:
    
    my_place_id = place['place_id']
    my_fields = ['name','type','vicinity','rating']
    place_details = map_client.place(place_id = my_place_id, fields = my_fields)
    
    #new_places = place_details.copy()
    
    
    
    

##for index in range(len(new_places)):
   ## if new_places[index]['result']['type'] == 'meal_delivery':
     ##   del new_places[index]        
     ##   break
        
#pprint('new places test')
pprint(place_details)


# json into dict
# parse dict to remove unwanted items
 