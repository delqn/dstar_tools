#!/usr/bin/env python

import struct
import zlib

from colors import colors

DRATS_HEAD = '[SOB]'
DRATS_TAIL = '[EOB]'
drats_head_len = len(DRATS_HEAD)
drats_tail_len = len(DRATS_TAIL)


DPRS_HEAD = '$GPGGA'
DPRS_TAIL = '\n'
dprs_head_len = len(DPRS_HEAD)
dprs_tail_len = len(DPRS_TAIL)


def __parse_drats_message(packet):
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


    for k,v in msg.iteritems():
        print '%s%s:  %s%s%s' % (colors.YELLOW, k, colors.BLUE, v, colors.X)

    return {'status': 'ok', 'message': msg}

def search_drats_message(buffer):
    if len(buffer) > drats_head_len + drats_tail_len \
      and DRATS_HEAD in buffer \
      and DRATS_TAIL in buffer[buffer.index(DRATS_HEAD):]:
        begin = buffer.index(DRATS_HEAD) + drats_head_len
        end = begin + buffer[begin:].index(DRATS_TAIL)
        message = __parse_drats_message(buffer[begin:end])
        buffer = buffer[:begin - drats_head_len] + buffer[end + drats_tail_len:]
        return (message, buffer)
    return (None, buffer)


def search_dprs_message(buffer):
    if len(buffer) > dprs_head_len + dprs_tail_len \
      and DPRS_HEAD in buffer \
      and DPRS_TAIL in buffer[buffer.index(DPRS_HEAD):]:
        begin = buffer.index(DPRS_HEAD)
        end = begin + buffer[begin:].index(DPRS_TAIL)
        message = buffer[begin:end]
        buffer = buffer[:begin] + buffer[end + dprs_tail_len:]
        return (message, buffer)
    return (None, buffer)
