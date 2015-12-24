import socket
import sys

from .colors import Colors
from .parser import Parser

MESSAGE_TYPE_PARSERS = (
    ('dprs', Parser.search_dprs_message),
    ('drats', Parser.search_drats_message),
)


class Monitor(object):
    def __init__(self, host, port, debug=False):
        self._host = host
        self._port = port
        self._debug = debug
        self._socket = socket.socket()
        self._connected = False

    def _dbg(self, *debug_messages):
        debug_message = ','.join(debug_messages)
        if self._debug:
            sys.stdout.write(
                '[Monitor {}{}{}] {}{}'.format(
                    Colors.GREEN, self._host, Colors.RESET, debug_message, Colors.RESET))

    def _connect(self):
        if not self._connected:
            self._dbg('connecting to socket')
            self._socket.connect((self._host, self._port))
            self._connected = True
            self._dbg('connected')

    def _get_buffer(self):
        self._connect()
        buffer_ = ''
        while self._socket:
            char = self._socket.recv(1)
            if not char or char == '\n':
                self._dbg('RECVd so far: {}{}\n'.format(Colors.RED, ''.join(buffer_)))
                break
            buffer_ += char

        return buffer_

    def read(self):
        buffer_ = self._get_buffer()
        messages = []
        for msg_type, parser in MESSAGE_TYPE_PARSERS:
            msg, buffer_ = parser(buffer_)
            if msg:
                messages.append((msg_type, msg))
        return messages
