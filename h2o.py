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
        title = "Drink water!",
        message = "For you health bro!",
        app_icon = "C:\\Users\\DELL\\Desktop\\drink water reminder\\icon.ico",
        timeout=12

     )
    time.sleep(60*60)