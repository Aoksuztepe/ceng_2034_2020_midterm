#!/usr/bin/python3.8

import os, threading, sys, time, requests



print("os name : " + str(os.name))
print("sys platform :" + str(sys.platform) + "\n" )
print("pID : " + str(os.getpid()) + "\n")
print("cpu count : " + str(os.cpu_count())+"\n")
print("LoadAvg : " + str(os.getloadavg()))




loadavg = os.getloadavg()
fiveMinuteLoadavg = loadavg[1]
FiveMinLoadAvg = "5 min.loadavg: " + str(fiveMinuteLoadavg)
print(FiveMinLoadAvg + "\n"+"\n")




urls = ['https://api.github.com', 'http://bilgisayar.mu.edu.tr/',
'https://www.python.org/', 'http://akrepnalan.com/ceng2034', 'https://github.com/caesarsalad/wow']

def status(urls):

        r = requests.get(urls)
        status_code = str(r)
        print(urls + "  " + status_code + " ")




start = time.time()

thread1 = threading.Thread(target=status, args=(urls[0],))
thread2 = threading.Thread(target=status, args=(urls[1],))
thread3 = threading.Thread(target=status, args=(urls[2],))
thread4 = threading.Thread(target=status, args=(urls[3],))
thread5 = threading.Thread(target=status, args=(urls[4],))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

finish = time.time()

print("\n" + "finished in: " + str(finish - start) + " seconds" +"\n")





result = "cpu count - 5. min.loadavg "

if os.cpu_count() - fiveMinuteLoadavg >= 1:
	print(result + "=  " + str(os.cpu_count() - fiveMinuteLoadavg))

else:
	print(result + "=  " + str(os.cpu_count() - fiveMinuteLoadavg))
	sys.exit()
