#!/usr/bin/env python

import threading
import time
import Queue

from dstartools import monitor

REFLECTORS = (
    ('alabama.ratflector.com', 9000),
    ('thailand.ratflector.com', 9001),
    ('cfl.ratflector.com', 9000),
    ('n1kxj.ratflector.com', 9000),
    ('ae5he.ratflector.com', 9000),
    ('wa7dr.ratflector.com', 9000),
    ('wa7fw.ratflector.com', 9000),
    ('gaares.ratflector.com', 9000),
    ('gwinnettares.ratflector.com', 9000),
    ('dcs007.ratflector.com', 9000),
    ('nfl.ratflector.com', 9000),
    ('nodig.ratflector.com', 9000),
    ('nwga.ratflector.com', 9000),
    ('pldares.ratflector.com', 9000),
    ('slc.ratflector.com', 9000),
    ('w5sf.ratflector.com', 9000),
    ('sewx.ratflector.com', 9000),
    ('stlouis.ratflector.com', 9000),
    ('sweden.ratflector.com', 9000),
    ('toledo.ratflector.com', 9000),
    ('W5SF.ratflector.com', 9000),
    ('wa7dre.ratflector.com', 9000),
    ('drats.ratflector.com', 9000),
    ('drats.ratflector.com', 9001),
)


q = Queue.Queue()


def go(host_, port_):
    mon = monitor.Monitor(host=host_, port=port_, debug=True)
    try:
        while True:
            q.put((host_, mon.read()))
    except IOError, e:
        print e.message

if __name__ == '__main__':
    monitors = []
    for host, port in REFLECTORS:
        threading.Thread(target=go, args=(host, port,)).start()

    while True:
        while not q.empty():
            print q.get()
        print "waiting 10 seconds"
        time.sleep(10)
