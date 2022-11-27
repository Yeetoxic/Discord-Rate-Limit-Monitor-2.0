#-------------------------------------------------------
#    DISCLAIMERS
#-----------------
#  DRLM2 is a program developed by Yeetoxic, please do not steal my code!
#  This program is protected under a MIT Lisense!
#-----------------

#  Copyright (c) 2022 Yeetoxic

#-------------------------------------------------------

#Imports
import os
import time
import requests
from threading import Thread

#Console Clear (OS COMMAND)
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#DRLM2 START Variable
START = 0

#Discord Rate Limit Monitor 2.0 (DRLM2)
def DRLM2():
  #StartUp Parameters
  global START
  global Lim
  global InitCheck
  if START == 0:
    START = 1
    Lim = 0
    InitCheck = 0

  #Discord API Requester
  r = requests.head(url="https://discord.com/api/v1")
  try:
    TH = (int(r.headers['Retry-After']) / 60) / 60
    TH = str(TH).split('.')[0]
    TM = (int(r.headers['Retry-After']) / 60) / 60
    TMD = TM % 1
    TM = TMD * 60
    TM = str(TM).split('.')[0]
    print(
      f"Rate limit found!\n\n    {TH} Hours & {TM} Minutes left\n\nPlease wait..."
    )
    Lim = 1
    InitCheck = 0
  except:
    if InitCheck == 0:
      FW = "No Current Rate Limiters from Discord API!"
      print(FW, end="\r")
      InitCheck = 1
      time.sleep(2)
      clearConsole()

  #API Connection Failure
  if Lim == 1:
    time.sleep(5)

    def RateKiller():
      global START
      global Lim
      global InitCheck
      START = 1
      Lim = 0
      InitCheck = 0
      clearConsole()
      print("Discord API process killed!\n\n Restarting!")
      time.sleep(10)
      os.system("kill 1")

    RateKiller()

  #Thread Automation
  DRLM2_T = Thread(target=DRLM2)
  DRLM2_T.start()