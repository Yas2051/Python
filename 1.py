import os, random
from datetime import datetime
from time import sleep, strftime

sciezka="C:\\Users\\mateu\\Desktop\\1\\test"

pliki=os.listdir(sciezka)
d=random.choice(pliki)
Przerwy = ["23:30:00","23:31:00","23:32:00"]
Lekcje =["23:30:30","23:31:30","23:32:30"]
PrzerwyIndex = 1
LekcjeIndex = 1
i = 1

while True:
    czas =  datetime.now()
    current_time = czas.strftime("%H:%M:%S")
    if i == 1 and current_time > Przerwy[PrzerwyIndex] and current_time < Lekcje[LekcjeIndex]:   
        print(Przerwy[PrzerwyIndex]) 
        i = 2        
        
    if i == 2:
        print(Lekcje[LekcjeIndex])
        i = 3
        
        sleep(0.1)

    if i == 3 and current_time > Lekcje[LekcjeIndex]:
        os.system('taskkill /f /im wmplayer.exe')  
        PrzerwyIndex = PrzerwyIndex + 1
        LekcjeIndex = LekcjeIndex + 1
        i = 1
    print(i)    
    print("Current Time =", current_time)
    sleep(1)