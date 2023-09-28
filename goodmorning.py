import time
timestamp = time.strftime('%H:%M:%S')
hour = time.strftime('%H')
minutes = time.strftime('%M')
seconds = time.strftime('%S')
if(int(hour)> 00 and int(minutes) > 00 and int(seconds) >00 and int(hour)< 12 and int(minutes) < 59 and int(seconds) < 59 ):
    print("GOOD MORNING SIR")
elif(int(hour)> 12 and int(minutes) > 59 and int(seconds) >59 and int(hour)< 5 and int(minutes) < 59 and int(seconds) < 59 ):
    print("GOOD EVENING SIR")
elif(int(hour)> 9 and int(minutes) > 00 and int(seconds) > 00 and int(hour)< 23 and int(minutes) < 59 and int(seconds) < 59 ):
    print("GOOD NIGHT SIR")
