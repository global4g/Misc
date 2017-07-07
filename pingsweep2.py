#!/usr/bin/python3

import multiprocessing
import subprocess
import os
import ipaddress
import sys 

#target = "10.1.1.0/30"


def pinger( job_q, results_q ):
    DEVNULL = open(os.devnull,'w')
    while True:
        ip = job_q.get()
        if ip is None: break

        try:
            subprocess.check_call(['ping','-c1',ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


if __name__ == '__main__':
    try:
        target = sys.argv[1]
    except:
        print("Usage : program [networkrange]")
        print("E.g.  : program 10.10.10.0/24")
        sys.exit(1)
    try:
    	net4 = ipaddress.ip_network(target)
    	print ("Processing ", net4.num_addresses)
    except Exception as ex:
       	print(ex)

    pool_size = net4.num_addresses 

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
             for i in range(pool_size) ]

    for p in pool:
        p.start()

    for i in net4.hosts():
        jobs.put(str(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    while not results.empty():
        ip = results.get()
        print(ip)
