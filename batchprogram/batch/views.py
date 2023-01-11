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
current_time=0.0
end=0.0
#counting=False
from batch.models import Enter_Leave

def home(request):
    #global now
    return render(request, 'HomeBatch.html', {'start': current_time, 'end': end})



def batchInRequest(request):
    global now
    global counting
    global end
    global current_time
    counting=True
    end=0.0
    print("hello world")
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    currenttime={str(current_time)}
    pyautogui.hotkey('f5')
    #enterleave=Enter_Leave(enter=current_time, leave=end)
    #enterleave.save()
    #webbrowser.open("http://127.0.0.1:8000/", new=0,autoraise=True)
    count(now,counting)
    #return render(request, 'HomeBatch.html', {'time': now})
    #! hello() 
    #! solange true wird die Zeit weitergezählt
    #return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
    return render(request, 'HomeBatch.html')

def batchOutRequest(request):
    global stop
    global end
    stop=True
    counting=False
    endd = datetime.now()
    end=endd.strftime("%m/%d/%Y, %H:%M:%S")
    pyautogui.hotkey('f5')
    enterleave=Enter_Leave(enter=current_time, leave=end)
    enterleave.save()
    #webbrowser.open("http://127.0.0.1:8000/",new=0, autoraise=True)
    #return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
    return render(request, 'HomeBatch.html')

def count(now,counting):
    while counting==True:
        global stop
        stop=False
        #self.loadNotificationCfg()
        ist=datetime.now()
        isttime=ist.strftime("%H:%M:%S")
        print(isttime)
        #end_time=time(hour=now.hour, minute=now.minute, second=now.second+2.0)
        end_time=now+timedelta(seconds=2)
        endtime=end_time.strftime("%H:%M:%S")
        #endtime=str(end_time)
        print(endtime)
        #end_time2=time(hour=now.hour, minute=now.minute, second=now.second+10.0)
        end_time2=now+timedelta(seconds=10)
        endtime2=end_time2.strftime("%H:%M:%S")
        #endtime2=str(end_time2)
        #end_time3=time(hour=now.hour, minute=now.minute, second=now.second+20.0)
        end_time3=now+timedelta(seconds=20)
        endtime3=end_time3.strftime("%H:%M:%S")
        #endtime3=str(end_time3)
        tim.sleep(1)
        if stop==True:
            ende=datetime.now()
            endetime=ende.strftime("%H:%M:%S")
            stop=False
            break
        if endtime == isttime:
            loadNotificationCfg()
            scheduleNotifications()
            #print("test1")
        elif endtime2 == isttime:
            loadNotificationCfg2()
            scheduleNotifications()
            #print("test2")
        elif endtime3 == isttime:
            loadNotificationCfg3()
            scheduleNotifications()
            #print("test3")
            now=0
            counting=False
            #break

"""
app=Flask(__name__)
@app.route('/')
def hello():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    currenttime=str(current_time)
    return render_template('HomeBatch.html',come="1234")
"""

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


