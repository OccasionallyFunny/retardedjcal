#!/usr/bin/python
import time,math
def IsLeapYear(nyear):
    return (nyear%33) in {1,5,9,13,17,22,26,30}
t = time.time() - 6751800 # 1349 new year
totaldays=0
day = 1
month = 1 
year = 1349

while (True) : 


    if (IsLeapYear(year)) :
        if(t<31622400):
            break
        t = t -31622400
        totaldays+=366
    else :
        if (t<3153600):
            break
        t = t  - 31536000
        totaldays+=365
    year +=1

while(True):
    if (month <7):
        if(t<2678400):
            break

        month +=1
        t = t-2678400
        totaldays+=31
    else:
        if(t<2592000):
            break

        month +=1
        t = t-2592000
        
        totaldays+=30

day = (math.ceil(t/86400))

totaldays+=day
print (f"{day}/{month}/{year}")
weekdays = ["Shanbe",
            "Yekshanbe",
            "Doshandbe",
            "Seshanbe",
            "Chaharshanbe",
            "Panjshanbe",
            "Jome"]
print(weekdays[(totaldays%7)-1])

