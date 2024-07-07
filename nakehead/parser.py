import json
import logging

 
def getCurrentPWM():
    file = open("nakehead_feeder.json")
    data_object = json.load(file)
    file.close()

    if data_object != None:
        print(data_object["startDate"])
        feederList = data_object["feeder"]
        for feeder in feederList :
            print(feeder["day"])
            print(feeder["pwmSpeed"])
            timerList = feeder["timers"]
            for timer in timerList: 
                print(timer["startTimer"])
                print(timer["endTimer"])
                print(timer["enable"])



getCurrentPWM()
 
