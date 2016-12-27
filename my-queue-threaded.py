#!/usr/bin/python
#http://www.troyfawkes.com/learn-python-multithreading-queues-basics/
'''
Modifed version, stops processing queue after certain conditions are met
'''

from Queue import Queue
from threading import  Thread
import time
import sys


#global
found=False

def setFound():
    global found
    found=True
    print "Found ***********"

def getFound():
    global found
    return found

def customFunc(x):
    #Write your awesome processing code here
    return

def do_stuff(q):
  while True:
    x = q.get()
    if not getFound():
        customFunc(x)
    if (x == 150000):
        setFound()
    q.task_done()

q = Queue(maxsize=0)


try:
    numThreads=int(sys.argv[1])
    print "Using %s Threads " % numThreads
except:
    numThreads=4
    print "Deafult Threads ", numThreads


t1=(time.time())
print "Starting Tests - Time is: %s\n" % t1

for i in range(numThreads):
  t = Thread(target=do_stuff, args=(q,))
  t.setDaemon(True)
  t.start();

for x in range(200000):
  q.put(x)
print "Queue Length at the beginning is", len(q.queue)

q.join();

t2=(time.time())
print "Ending Tests - Time is: %s\n" % t2
print "Total Time %s" % (t2-t1)

