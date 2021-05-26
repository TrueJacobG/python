def make_readable(seconds):
    hour = int(seconds/60/60)
    if hour >= 1:
        seconds = seconds - (hour*60*60)
    if hour < 10:
        hour = "0"+str(hour)
    minute = int(seconds/60)
    if minute >= 1:
        seconds = seconds - (minute*60)
    if minute < 10:
        minute = "0"+str(minute)
    if seconds < 10:
        seconds = "0"+str(seconds)
    return str(hour)+":"+str(minute)+":"+str(seconds)


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
