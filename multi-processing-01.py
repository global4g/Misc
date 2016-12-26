#!/usr/bin/python
#http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
'''
MultiProcessing Examples
'''
import sys
import time
from multiprocessing.dummy import Pool as ThreadPool
import urllib2
urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.google.com',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://www.apple.com'
  ]

try:
   numThreads=int(sys.argv[1])
except:
   numThreads=4
   print "Deafult Threads ", numThreads



def myTest1():
    x=(time.time())
    print "Starting Time is: %s" % x
    pool = ThreadPool(numThreads)

    #Open the URLS in their own threads and populate the results
    results = pool.map(urllib2.urlopen, urls)

    pool.close()
    pool.join()

    y=(time.time())
    print "Ending Time is: %s" %y
    print "Total Time\n", y-x

def customFunc(parm):
    if (len(parm) > 25):
        return (parm, len(parm))

def myTest2():
    pool = ThreadPool(numThreads)

    #Open the URLS in their own threads and populate the results
    results = pool.map(customFunc, urls)

    pool.close()
    pool.join()

    print "\n"
    print results;
    print "\n"
    print filter(None, results)


myTest1()
myTest2()

