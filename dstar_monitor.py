#!/usr/bin/env python

import argparse
import socket
import sys

from mock_dstar_socket import MockDRatsSocket

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('host_name', metavar='HOST_NAME', type=str, help='Host Name')
parser.add_argument('port_number', metavar='PORT_NUMBER', type=int, help='Port Number')
parser.add_argument('--testing', metavar='TESTING', type=bool, help='Unit Testing', default=False)
args = parser.parse_args()

print args.host_name
print args.port_number

class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    X = '\033[0m'

# jerry-rigged testing
if args.testing == True:
    s = MockDRatsSocket()
else:
    s = socket.socket()
    s.connect((args.host_name, args.port_number))

found_beginning = False
body_array = []
messages = []


def search_drats_message(buffer):
    HEAD = '[SOB]'
    TAIL = '[EOB]'
    head_tail_length = len(HEAD) + len(TAIL)
    if len(buffer) > head_tail_length and HEAD in buffer and TAIL in buffer[buffer.index(HEAD):]:
        message_start = buffer.index(HEAD) + len(HEAD)
        message_end = buffer[message_start:].index(TAIL)
        print "message_start", message_start
        print "message_end", message_end
        message = buffer[message_start:message_end]
        buffer = buffer[:message_start] + buffer[message_end + len(TAIL):]
        return (message, buffer)
    return (None, buffer)

def search_dprs_message(buffer):
    HEAD = "$GPGGA"
    TAIL = "\n"
    head_tail_length = len(HEAD) + len(TAIL)
    if len(buffer) > head_tail_length and HEAD in buffer and TAIL in buffer:
        message = buffer[ buffer.index(HEAD):buffer.index(TAIL) ]
        buffer = buffer[:buffer.index(HEAD)] + buffer[buffer.index(TAIL) + len(TAIL):]
        return (message, buffer)
    return (None, buffer)

understandable_messages = {
    'dprs': search_dprs_message,
    'drats': search_drats_message
}

while s:
    char = s.recv(1)
    if not char: break
    body_array.append(char)
    buffer = ''.join(body_array)
    sys.stdout.write('RECVd so far: %s%s%s\n' % (colors.RED, ''.join(buffer), colors.X))

    for message_type, function in understandable_messages.iteritems():
        print "Searching for %s" % message_type
        message, buffer = function(buffer)
        if message:
            print "%sFound %s string: %s%s%s" % (
                colors.GREEN,
                message_type,
                colors.BLUE,
                message,
                colors.X)
        print "Buffer: %s%s%s" % (colors.RED, buffer, colors.X)
        messages.append((message_type, message))
