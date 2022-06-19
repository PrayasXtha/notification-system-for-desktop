from email import message
import imp
from socket import timeout
import time
from tkinter.tix import MAIN
from turtle import title
from pip import main
from plyer import notification

if __name__ == "__main__":
   while True:
    notification.notify(
        title = "Drink water!", #change the notification title here
        message = "For you health bro!", #change the message here
        app_icon = "C:\\Users\\DELL\\Desktop\\drink water reminder\\icon.ico", #use the your icon path here
        timeout=12 #timeout denotes the time span the meaage will pop for

     )
    time.sleep(60*60) #time sleep denotes the time interval between the nofication, here its set for every 1 hrs 1 notification
