import time
start_time = time.time()
for i in range(5):
    time.sleep(1.2)
    print('Come on, you can do it.')
end_time = time.ctime()
time_consume = time.time() - start_time
print('Time you spent: ' + str(time_consume) +'s.')
print('You complete the challenge at ' + end_time)

# Write to file
f = open('record.csv','a')
f.write(str(time_consume) + ' , ' + end_time + '\n')
f.close()


