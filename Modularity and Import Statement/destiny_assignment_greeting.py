import time
def greet():
    localtime = time.localtime()
    hour = localtime.tm_hour
    if hour < 12:
     print("Good morning Kefas Lungu!")
    elif hour < 16:
     print("Good afternoon Kefas Lungu!")
    else:
     print("Good evening Kefas Lungu!")

greet()         