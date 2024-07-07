import json
import logging

 
def getCurrentPWM(startDay, currnetNumberOfFish):
    file = open("nakehead_feeder.json")
    data_object = json.load(file)
    file.close()
    # "startDate": "02/06/2024",
    print(startDay)
    if data_object != None:
        
        feederList = data_object["feeder"]
        for feeder in feederList :
            print(feeder["day"])
            print(feeder["pwmSpeed"])
            timerList = feeder["timers"]
            for timer in timerList: 
                print(timer["startTimer"])
                print(timer["endTimer"])
                print(timer["enable"])


startDate="02/06/2024"
currnetNumberOfFish = 2000
getCurrentPWM(startDate, currnetNumberOfFish)
 
