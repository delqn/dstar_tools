#!/usr/bin/env python

import enum
import struct
import zlib

from .colors import Colors


class MessageType(enum.Enum):
    drats = 'drats'
    dprs = 'dprs'

# type: head, tail
BOOKENDS = {
    MessageType.drats: ('[SOB]', '[EOB]'),
    MessageType.dprs: ('$GPGGA', '\n'),
}


class Parser(object):
    @classmethod
    def search_drats_message(cls, buff):
        head, tail = BOOKENDS.get(MessageType.drats)
        if not _is_valid(MessageType.drats, buff):
            return (None, buff)
        start = buff.index(head) + len(head)
        end = start + buff[start:].index(tail)
        message = _parse_drats_message(buff[start:end])
        return (message, buff[:start - len(head)] + buff[end + len(tail):])

    @classmethod
    def search_dprs_message(cls, buff):
        head, tail = BOOKENDS.get(MessageType.dprs)
        if not _is_valid(MessageType.dprs, buff):
            return (None, buff)
        start = buff.index(head)
        end = start + buff[start:].index(tail)
        message = buff[start:end]
        return (message, buff[:start] + buff[end + len(tail):])


def _is_valid(msg_type, buff):
    head, tail = BOOKENDS.get(msg_type)
    return (buff and
            len(buff) > len(head) + len(tail) and
            head in buff and
            tail in buff[buff.index(head):])


def _parse_drats_message(packet):
    msg = {'raw_data': packet}

    if ord(packet[0]) not in (0xDD, 0x22):
        return {'status': 'error', 'message': None}

    # add data
    if ord(packet[0]) == 0xDD:
        msg['is_compressed'] = True
        msg['data'] = zlib.decompress(packet[25:])
    else:
        msg['is_compressed'] = False
        msg['data'] = packet[25:]

    # unpack header
    ordered_value_names = ('magic_number',
                           'sequence',
                           'session',
                           'message_type',
                           'checksum',
                           'length',
                           'source',
                           'destination')

    STRUCT_FORMAT = "!BHBBHH8s8s"
    msg.update(dict(zip(ordered_value_names,
                        struct.unpack(STRUCT_FORMAT, packet[:25]))))

    # TODO(delyan): CRC calculations and comparison here

    for k, v in msg.iteritems():
        print '{}{}:  {}{}{}'.format(Colors.YELLOW, k, Colors.BLUE, v, Colors.RESET)

    return {'status': 'ok', 'message': msg}
