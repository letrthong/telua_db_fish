import json
import logging
import time
import datetime
import uuid
from datetime import timezone
import logging 

def getCurrentPWM(startDay, offset_time , currnetNumberOfFish, config_file_path):
    epoch_time = int(time.time()) + offset_time
    print("epoch_time=" + str(epoch_time )  )
    
    # "startDate": "02/06/2024" -dd-mm-yyyy,
    datetime_object = datetime.datetime.strptime(startDay, "%d/%m/%Y") 
    print(datetime_object) 
    total_seconds = datetime_object.timestamp()
    print("timestamp=" + str( total_seconds ) )

    second_next_day = epoch_time  - total_seconds

    next_day = int( second_next_day/(3600*24)) + 1
    print("next_day=" + str(next_day))
 
    file = open(config_file_path)
    data_object = json.load(file)
    file.close()
    # "startDate": "02/06/2024",
    print(startDay)

    scheduler_array = []
    count = 0
    if data_object != None:
        config_list = data_object["Configs"]
        numberOfFish =  data_object["numberOfFish"]
        for config in config_list :
            day =  config["day"]
            if day == next_day:
                print("")
                print("Day=" + str( day))

                print(config["pwmSpeed"])

                feederTimerList = config["feederTimers"]
                for feederTimer in feederTimerList: 
                    startTimer = feederTimer["startTimer"]
                    endTimer = feederTimer["endTimer"]
                    enable = feederTimer["enable"]
                    if enable == True:  
                        print("\n" + startTimer)
                        print(endTimer)

                        end_time = get_hour_by_number_of_fish( currnetNumberOfFish,numberOfFish,  startTimer, endTimer)
                        print("end_time=" +  end_time)
                        scheduler_item  = {
                            "id": "2024-"+ str(uuid.uuid1()),
                            "month": "0",
                            "action": "70",
                            "enable": True,
                            "repeat": "daily",
                            "stopTimer": endTimer  ,
                            "startTimer": startTimer,
                            "levelSwitch": ""
                        }
                        count = count+ 1
                        scheduler_array.append(scheduler_item)
    if  count > 0:
        return scheduler_array
    return None

    # scheduler_string = json.dumps(scheduler_array)
    # print("scheduler_string=" + scheduler_string)
    # return scheduler_string

    
 
def convert_hour_mm_ss_2_second(time_str):
    if len(time_str) == 5:
        h, m  = time_str.split(':')
        return int(h) * 3600 + int(m) * 60

    if len(time_str) == 8:
        h, m,s  = time_str.split(':')
        return ( int(h) * 3600) + (int(m) * 60) + int(s)

    return 0

 
def get_hour_by_number_of_fish(currnetNumberOfFish, numberOfFish, start_hh_mm_ss, end_hh_mm_ss):
    print("get_hour_by_number_of_fish currnetNumberOfFish/numberOfFish=" + str( currnetNumberOfFish) +  "/" + str(numberOfFish ) )
    feedertimer = 1 
    if currnetNumberOfFish > numberOfFish and currnetNumberOfFish <  (numberOfFish*10) :
        feedertimer =  currnetNumberOfFish/numberOfFish

    total_seconds =  convert_hour_mm_ss_2_second(end_hh_mm_ss) - convert_hour_mm_ss_2_second(start_hh_mm_ss)

    total_seconds = int(total_seconds*feedertimer)
    print("get_hour_by_number_of_fish total_seconds=" + str( total_seconds))
    end_time = time.strftime('%H:%M:%S', time.gmtime(convert_hour_mm_ss_2_second(start_hh_mm_ss) + total_seconds ))
    return str(end_time)

 
startDate="01/06/2024"
currnetNumberOfFish = 2000
config_file_path= "nakehead_phase3.json"

getCurrentPWM(startDate, currnetNumberOfFish, config_file_path)


# startDate="01/06/2024"
# currnetNumberOfFish = 1000
# getCurrentPWM(startDate, currnetNumberOfFish, config_file_path)

# startDate="07/07/2024"
# currnetNumberOfFish = 2000
# getCurrentPWM(startDate, currnetNumberOfFish, config_file_path)