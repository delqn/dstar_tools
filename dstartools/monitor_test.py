import unittest

from .monitor import Monitor
from .mocks import MockDRatsSocket


class MonitorTest(unittest.TestCase):
    def setUp(self):
        self._monitor = Monitor(host='a', port=123)
        self._monitor._socket = MockDRatsSocket()

    def test_monitor(self):
        for _ in range(3):
            messages = self._monitor.read()
        expected = (
            'drats', {
                'status': 'ok',
                'message': {
                    'magic_number': 34,
                    'sequence': 15680,
                    'raw_data': ('"=@=@=@n=@YN0DEC~~~CQCQCQ~~[QST] Sheboygan, (WI) Weather Info & '
                                 'Ratflector - Network, host: 59.54.54.53, port 8801'),
                    'destination': '~~CQCQCQ',
                    'is_compressed': False,
                    'length': 28221,
                    'session': 61,
                    'source': '@YN0DEC~',
                    'checksum': 15680,
                    'data': ('~~[QST] Sheboygan, (WI) Weather Info & Ratflector'
                             ' - Network, host: 59.54.54.53, port 8801'),
                    'message_type': 64}})
        self.assertEqual(messages, [expected])
