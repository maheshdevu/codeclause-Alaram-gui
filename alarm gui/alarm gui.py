import datetime
from playsound import playsound
AlaramHour = int(input("Enter Hour: "))
AlaramMin = int(input("Enter Min: "))
AlaramAm = input("am / pm: ")

if AlaramAm=="pm":
    AlaramHour+=12
while True:
    if AlaramHour==datetime.datetime.now().hour and AlaramMin==datetime.datetime.now().minute:
        print("playing..")
        playsound("C:\\Users\\MAHESH\\Downloads\\mixkit-alarm-tone-996.wav")
        break
