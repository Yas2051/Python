import os, random
from datetime import datetime
from time import sleep, strftime

sciezka="C:\\Users\\mateu\\Desktop\\1\\test" # sciezka plikow
# -------------------------------------------------
pliki=os.listdir(sciezka) # lista plikow w sciezce
d=random.choice(pliki) # wybieramy losowy plik z sciezki
# -------------------------------------------------
# tabele z przerwami i lekcjami
Przerwy = ["23:30:00","23:31:00","23:32:00"] # Godziny o ktorej zaczynaja sie przerwy
Lekcje =["23:30:30","23:31:30","23:32:30"] # Godziny kiedy zaczynaja sie lekcje
# -------------------------------------------------
#indexy poczatkowe
PrzerwyIndex = 1  # numer przerwy
LekcjeIndex = 1 # numer lekcji
i = 1 # odpowiada aktualnej pozycji w petli
# -------------------------------------------------

# petla ktora sprawdza czas
while True:
    czas =  datetime.now() # aktualna godzina

    current_time = czas.strftime("%H:%M:%S") # formatowanie godziny

    # petla sprwadzajaca index 
    if i == 1 and current_time > Przerwy[PrzerwyIndex] and current_time < Lekcje[LekcjeIndex]:   # sprawdza aktualna pozycje w petli i sprawdza czy aktualnie jest przerwa
        print(Przerwy[PrzerwyIndex]) 
        i = 2        
        os.startfile(d) # odpalamy losowy plik z danej sciezki
# -------------------------------------------------    
    
    # testowe pokazuje czas wylaczenia
    if i == 2:
        print(Lekcje[LekcjeIndex])
        i = 3
        
        sleep(0.1)
# -------------------------------------------------

    #wylaczamy program gdy skonczy sie przerwa
    if i == 3 and current_time > Lekcje[LekcjeIndex]: # sprawdza aktualna pozycje w petli i sprawdza czy przerwa sie skonczyla
        os.system('taskkill /f /im wmplayer.exe')  # wylacza program
        PrzerwyIndex = PrzerwyIndex + 1 # zmienia index przerwy oraz lekcji na nastepny, co umozliwia sledzenie ktora jest lekcja
        LekcjeIndex = LekcjeIndex + 1
        i = 1
# -------------------------------------------------
# debug        
    print(i)    
    print("Aktualna Godzina =", current_time)
    sleep(1)