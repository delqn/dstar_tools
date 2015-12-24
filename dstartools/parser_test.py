import unittest

from .parser import Parser
from .mocks import MockDRatsSocket


UNDERSTANDABLE_MESSAGES = {
    'dprs': Parser.search_dprs_message,
    'drats': Parser.search_drats_message
}


class ParserTest(unittest.TestCase):
    def setUp(self):
        self._socket = MockDRatsSocket()

    def _get_buffer(self):
        buffer_ = ''
        while self._socket:
            char = self._socket.recv(1)
            if not char:
                break
            buffer_ += char
        return buffer_

    def test_dprs_message_parser(self):
        buffer_ = self._get_buffer()
        messages = Parser.search_dprs_message(buffer_)
        expected_message = '$GPGGA,002442,4003.726,N,7505.448,W,1,3,0,0,M,0,M,,*76'
        self.assertIn(expected_message, messages)

    def test_drats_message_parser(self):
        buffer_ = self._get_buffer()
        messages, buffer_ = Parser.search_drats_message(buffer_)
        expected_message = {
            'status': 'ok',
            'message': {
                'magic_number': 34,
                'sequence': 15680,
                'checksum': 15680,
                'destination': '~~CQCQCQ',
                'is_compressed': False,
                'length': 28221,
                'session': 61,
                'source': '@YN0DEC~',
                'data': ('~~[QST] Sheboygan, (WI) Weather Info & Ratflector - '
                         'Network, host: 59.54.54.53, port 8801'),
                'raw_data': ('"=@=@=@n=@YN0DEC~~~CQCQCQ~~[QST] Sheboygan, (WI) Weather Info & '
                             'Ratflector - Network, host: 59.54.54.53, port 8801'),
                'message_type': 64
            }
        }
        self.assertEqual(expected_message, messages)
