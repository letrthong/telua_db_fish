import json
import logging
import time
import datetime
from datetime import timezone
 
def getCurrentPWM(startDay, currnetNumberOfFish):
    epoch_time = int(time.time())
    print("epoch_time=" + str(epoch_time )  )
    
    # "startDate": "02/06/2024" -dd-mm-yyyy,
    datetime_object = datetime.datetime.strptime(startDay, "%d/%m/%Y") 
    print(datetime_object) 
    total_seconds = datetime_object.timestamp()
    print("timestamp=" + str( total_seconds ) )

    second_next_day = epoch_time  - total_seconds

    next_day = int( second_next_day/(3600*24)) + 1
    print("next_day=" + str(next_day))
 
    file = open("nakehead_feeder.json")
    data_object = json.load(file)
    file.close()
    # "startDate": "02/06/2024",
    print(startDay)
    if data_object != None:
        
        feederList = data_object["feeder"]
        for feeder in feederList :
            day =  feeder["day"]
            if day == next_day:
                print("")
                print("Day=" + str( day))
                print(feeder["pwmSpeed"])
                timerList = feeder["timers"]
                for timer in timerList: 
                    print("\n" + timer["startTimer"])
                    print(timer["endTimer"])
                    print(timer["enable"])


startDate="01/06/2024"
currnetNumberOfFish = 2000
getCurrentPWM(startDate, currnetNumberOfFish)
 
# startDate="07/07/2024"
# currnetNumberOfFish = 2000
# getCurrentPWM(startDate, currnetNumberOfFish)