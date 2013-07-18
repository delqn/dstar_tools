#!/usr/bin/env python

import argparse
import socket
import sys

import message_parsers
from colors import colors
from mock_dstar_socket import MockDRatsSocket

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('host_name', metavar='HOST_NAME', type=str, help='Host Name')
parser.add_argument('port_number', metavar='PORT_NUMBER', type=int, help='Port Number')
parser.add_argument('--testing', metavar='TESTING', type=bool, help='Unit Testing', default=False)
args = parser.parse_args()

print args.host_name
print args.port_number

# jerry-rigged testing
if args.testing:
    s = MockDRatsSocket()
else:
    s = socket.socket()
    s.connect((args.host_name, args.port_number))

found_beginning = False
bffr = ''
messages = []

understandable_messages = {
    'dprs': message_parsers.search_dprs_message,
    'drats': message_parsers.search_drats_message
}

while s:
    char = s.recv(1)
    if not char: break
    bffr += char
    #sys.stdout.write('RECVd so far: %s%s%s\n' % (colors.RED, ''.join(bffr), colors.X))

    for message_type, function in understandable_messages.iteritems():
        message, bffr = function(bffr)
        if message:
            messages.append((message_type, message))

if args.testing:
    print "Test Results:"
    print "\tDPRS ok: ", ('dprs', '$GPGGA,002442,4003.726,N,7505.448,W,1,3,0,0,M,0,M,,*76') in messages
    message = {'status': 'ok', 'message': {'magic_number': 34, 'sequence': 15680, 'checksum': 15680, 'destination': '~~CQCQCQ', 'is_compressed': False, 'length': 28221, 'session': 61, 'source': '@YN0DEC~', 'data': '~~[QST] Sheboygan, (WI) Weather Info & Ratflector - Network, host: 59.54.54.53, port 8801', 'message_type': 64}}
    print "\tDRATS uncompressed ok: ", ('drats',message) in messages

    message = {'status': 'ok', 'message': {'magic_number': 221, 'sequence': 15680, 'checksum': 15680, 'destination': '~~CQCQCQ', 'is_compressed': True, 'length': 28221, 'session': 61, 'source': '@YN0DEC~', 'data': '~~[QST] Sheboygan, (WI) Weather Info & Ratflector - Network, host: 59.54.54.53, port 8801', 'message_type': 64}}
    print "\tDRATS compressed ok: ", ('drats',message) in messages
