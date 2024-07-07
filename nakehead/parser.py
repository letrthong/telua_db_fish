import json
import logging
import time
import datetime
from datetime import timezone
 
def getCurrentPWM(startDay, currnetNumberOfFish):
    epoch_time = int(time.time())
    print(epoch_time)


    file = open("nakehead_feeder.json")
    data_object = json.load(file)
    file.close()
    # "startDate": "02/06/2024",
    print(startDay)
    if data_object != None:
        
        feederList = data_object["feeder"]
        for feeder in feederList :
            print("")
            print("Day=" + str( feeder["day"] ) )
            print(feeder["pwmSpeed"])
            timerList = feeder["timers"]
            for timer in timerList: 
                print("\n" + timer["startTimer"])
                print(timer["endTimer"])
                print(timer["enable"])


startDate="01/06/2024"
currnetNumberOfFish = 2000
getCurrentPWM(startDate, currnetNumberOfFish)
 
