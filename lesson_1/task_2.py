time = int(input("Enter time in seconds"))
hours = time // 3600
minutes = (time // 60) % 60
seconds = time % 60
if  hours < 10:
    hours = str("0") + str(hours)
if  minutes < 10:
    minutes = str("0") + str(minutes)
if  seconds < 10:
    seconds = str("0") + str(seconds)
print(f"часы: {hours}, минуты: {minutes}, секунды: {seconds}")


