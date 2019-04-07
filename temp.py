import datetime, time

starttime = datetime.datetime.now()

for i in range(10):
    time.sleep(0.3)

endtime = datetime.datetime.now()

print (endtime - starttime).seconds

