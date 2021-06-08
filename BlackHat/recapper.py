# -*- coding: utf-8 -*-

from scapy.all import TCP, rdpcap
import collections
import os
import re
import sys
import zlib

OUTDIR = 'pictures'
PCAPS = '/mydownlods'

Response = collections.namedtuple('Response', ['header', 'payload'])


def get_header(payload):
    try:
        header_raw = payload[:payload.index(b'\r\n\r\n')+2]
    except ValueError:
        sys.stdout.write('-')
        sys.stdout.flush()
        return None

    header = dict(re.findall(r'(?P<name>.*?):(?P<value>.*?)\r\n', header_raw.decode()))
    if 'Content-Type' not in header:
        return None
    return header