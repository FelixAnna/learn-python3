#! /usr/bin/env python3

"""
This part shows you
how to use thread in python3
_thread : one way to start thread without create class
threading : recommand way to start thread with class inherit threading.Thread
queue: which is ensure thread safe
"""

import _thread
import time

finished=0
def print_progress(threadId, speed):
    i,total=0,100
    while i<total:
        print("Thread {} have finished {}%...".format(threadId, i))
        i+=speed
        time.sleep(0.1)
    else:
        global finished
        finished+=1
        print("Thread {0} have done.".format(threadId))


try:
    _thread.start_new_thread(print_progress, ('ThreadA',10))
    _thread.start_new_thread(print_progress, ('ThreadB',8))
except:
    print("Error: cannot start any thread.")

#recomand way
import threading

while 1:
    if(finished==2):
        print("They have been finished.")
        break

class Download(threading.Thread):
    def __init__(self, threadId, speed):
        threading.Thread.__init__(self)
        self.threadId=threadId
        self.speed=speed

    def run(self):
        print("Thread {} start running with speed {}...".format(self.threadId, self.speed))

        thlock.acquire()
        print_progress(self.threadId,self.speed)
        thlock.release()

        print("Thread {} finished.".format(self.threadId))

thlock=threading.Lock()

tha=Download("ThA", 36)
thb=Download("ThB", 17)
thc=Download("ThC", 12)

threads=[tha,thb]
threads.append(thc)

for th in threads:
    th.start()

print("I am in the main thread {},totally we have active threads: {}.".format(threading.currentThread(), threading.activeCount()))

for th in threads:
    th.join()


import queue
import random

class Calculator(threading.Thread):
    def __init__(self, name, op, q):
        threading.Thread.__init__(self)
        self.name=name
        self.op=op
        self.q=q

    def run(self):
        while not exitFlag:
            #print("{}-{}-{}".format(self.name, self.op, self.q.empty()))
            lock.acquire()
            if not self.q.empty():
                val=int(self.q.get())
                lock.release()
                if self.op=='**':
                    print("{0}**{0} is {1} in {2}".format(val, val**val,self.name))
                else:
                    print("{0}sqrt{1} is {2} in {3}".format(val, -1*val, val**(1/val),self.name))
            else:
                lock.release()
            time.sleep(1)


exitFlag=0
wq=queue.Queue()
lock=threading.Lock()
threads=[]

for i in range(5):
    if i%3==0:
        op="**"
    else:
        op="sqrt"
    thread=Calculator("Th{}".format(i), op,wq)
    thread.start()
    threads.append(thread)

print("start assign queue...")
lock.acquire()
for i in range(20):
    wq.put(str(random.randrange(1,10)))
lock.release()

print("queue size is: ",repr(wq.qsize()))

while not wq.empty():
    pass

exitFlag=1

for th in threads:
    th.join()

print("Done")


            
#thread with queue
