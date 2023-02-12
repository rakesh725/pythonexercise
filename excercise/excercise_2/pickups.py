
import json

def getTruckByType(type):
    #load json file 
    with open("./pickups.json", 'r') as j:
     pickup_trucks = json.loads(j.read())
    #look for pickup by type 

    for pickups in pickup_trucks:
        print(pickups)
