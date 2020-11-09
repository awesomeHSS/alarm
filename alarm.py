import os
import datetime

os.system("cls")
alarm = input("Saat:Dakika:Saniye:")

while True:
    an = datetime.datetime.now()
    saat = datetime.datetime.strftime(an,'%X' )
    if saat == alarm:
        os.startfile(r"C:\Users\ASUS\Downloads\Alarm.mp3")