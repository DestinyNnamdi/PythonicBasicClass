import datetime
def greet():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if hour < 12:
     print("Good morning Kefas James Lungu!")
    elif hour < 16:
     print("Good afternoon Kefas James Lungu!")
    else:
     print("Good evening Kefas James Lungu!")

greet()