from datetime import datetime, timedelta, time
now = datetime.now() # save current time to now parameter
current_time = now.strftime("%m/%d/%Y, %H:%M:%S") # change time format
currenttime={str(current_time)}