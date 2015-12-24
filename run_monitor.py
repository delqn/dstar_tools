#!/usr/bin/env python

import argparse

from dstartools import monitor


argparser = argparse.ArgumentParser(description='Process some integers.')
argparser.add_argument('host_name', metavar='HOST_NAME', type=str, help='Host Name')
argparser.add_argument('port_number', metavar='PORT_NUMBER', type=int, help='Port Number')

args = argparser.parse_args()

mon = monitor.Monitor(host=args.host_name, port=args.port_number, debug=True)

counter = 0

if __name__ == '__main__':
    while True:
        counter += 1
        print mon.read()
