from django.shortcuts import render
from django.http import HttpResponse
import json
from notifypy import Notify
import time as tim
import schedule
from datetime import datetime, timedelta, time
import sys
#from flask import Flask, render_template
#import webbrowser
import pyautogui
# Create your views here.
#counting=False
from batch.models import Enter_Leave

current_time=0.0
end=0.0
breakstop=False
stopbreak = datetime.now()-datetime.now() # need to be defined here becaus count function is first function which requires it not break function
startbreak= datetime.now()-datetime.now() # need to be defined here becaus count function is first function which requires it not break function
duringbreak=False

def home(request):
    return render(request, 'HomeBatch.html', {'start': current_time, 'end': end})

def batchInRequest(request):
    global now
    global counting
    global end
    global current_time
    end=0.0
    counting=True
    now = datetime.now() # save current time to now parameter
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S") # change time format
    pyautogui.hotkey('f5') # update the browser page
    count(now) # send the time at which you batched in to the count function
    return render(request, 'HomeBatch.html')

def batchOutRequest(request):
    global stop
    global end
    stop=True
    counting=False
    endd = datetime.now() #store the batch out time in endd parameter
    end=endd.strftime("%m/%d/%Y, %H:%M:%S") # change endd time format
    pyautogui.hotkey('f5') # update the current browser page
    enterleave=Enter_Leave(enter=current_time, leave=end) # request to store the start end end time
    enterleave.save()
    return render(request, 'HomeBatch.html', {'start': current_time, 'end': end})

def count(now):
    global counting
    while counting==True:
        global stop
        global breakstop
        global isttime
        global endtime
        global endtime2
        global endtime3
        global duringbreak
        stop=False
        while duringbreak==True: #pause the program during break
            tim.sleep(1) # without an statement this loop is not working
        ist=datetime.now() #update the current time ever sw-cycle
        isttime=ist.strftime("%H:%M:%S")
        if breakstop==True:
            breaktime = stopbreak - startbreak
        else:
            breaktime = datetime.now()-datetime.now() #no breaktime to be added
        end_time=now+timedelta(seconds=10)+breaktime # add the breaktime to the endtime, breaktime i 0 if no break was done
        endtime=end_time.strftime("%H:%M:%S")
        end_time2=now+timedelta(seconds=20)+breaktime
        endtime2=end_time2.strftime("%H:%M:%S")
        end_time3=now+timedelta(seconds=30)+breaktime
        endtime3=end_time3.strftime("%H:%M:%S")
        tim.sleep(1) # time delay is required as time is just stored in seconds. So every milisecont the if following if satements are true. As a result without that delay a lot of notifications are triggered
        if stop==True: # this is true by pushing batch out
            ende=datetime.now() # save time at batch out time
            endetime=ende.strftime("%H:%M:%S")
            stop=False
            break
        if endtime == isttime: # this is true after 8h
            loadNotificationCfg()
            scheduleNotifications()
        elif endtime2 == isttime: # this is true after 8,5h
            loadNotificationCfg2()
            scheduleNotifications()
        elif endtime3 == isttime: # this is true after 9,5h
            loadNotificationCfg3()
            scheduleNotifications()
            now=0
            counting=False #finish counting loop because last reminder is send

def batchBreakRequestStart(request):
    global breakstop
    global stopbreak
    global startbreak
    global duringbreak
    duringbreak=True
    breakstop=False
    startbreak=datetime.now()
    return render(request, 'HomeBatch.html', {'start': current_time, 'end': end})

def batchBreakRequestStop(request):
    global breakstop
    global stopbreak
    global duringbreak
    duringbreak=False
    breakstop=True
    stopbreak=datetime.now()
    #stopbreaktime=stopbreak.strftime("%H:%M:%S")
    return render(request, 'HomeBatch.html', {'start': current_time, 'end': end})

def loadNotificationCfg():
    global notificationCfg
    json_datei = open("notification.json", "r")
    json_text = ''
    for zeile in json_datei:
        json_text += zeile   
    notificationCfg = json.loads(json_text)
        #print(json_text)
    
def loadNotificationCfg2():
    global notificationCfg
    json_datei = open("notification2.json", "r")
    json_text = ''
    for zeile in json_datei:
        json_text += zeile        
    notificationCfg = json.loads(json_text)
    
def loadNotificationCfg3():
    global notificationCfg
    json_datei = open("notification3.json", "r")
    json_text = ''
    for zeile in json_datei:
        json_text += zeile   
    notificationCfg = json.loads(json_text)
    
    
def scheduleNotifications():
    global notification
    for notification in notificationCfg:
       notify(notification)
    
def notify(data):
    notification = Notify()
    notification.application_name = "TimeProgram"
    notification.title = data['title']
    notification.message = data['text']
    notification.send(block=False)


