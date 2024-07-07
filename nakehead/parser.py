import json
import logging

 
file = open("nakehead_feeder.json")
data_object = json.load(file)
file.close()

if data_object != None:
    print(data_object["startDate"])

 
