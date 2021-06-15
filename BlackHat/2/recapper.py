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
    # 从解码后的有效载荷中创建一个字典（header），在冒号上进行分割，使键是冒号之前的部分，值是冒号之后的部分
    header = dict(re.findall(r'(?P<name>.*?):(?P<value>.*?)\r\n', header_raw.decode()))
    if 'Content-Type' not in header:
        return None
    return header


def extract_content(Response, content_name='image'):
    content, content_type = None, None
    if content_name in Response.header['Content-Type']:
        content_type = Response.header['Content-Type'].split('/')[1]
        content = Response.payload[Response.payload.index(b'\r\n\r\n')+4:]

        if 'Content-Encoding' in Response.header:
            if Response.header['Content-Encoding'] == "gzip":
                content = zlib.decompress(Response.payload, zlib.MAX_WBITS | 32)
            elif Response.header['Content-Encoding'] == "deflate":
                content = zlib.decompress(Response.payload)

    return content, content_type


class Recapper:
    def __init__(self, fname):
        pcap = rdpcap(fname)
        self.sessions = pcap.sessions()
        self.response = list()

    def get_response(self):
        for session in self.sessions:
            payload = b''
            for packet in self.sessions[session]:
                try:
                    if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                        payload += bytes(packet[TCP].payload)
                except IndexError:
                    sys.stdout.write(x)
                    sys.stdout.flush()

            if payload:
                header = get_header(payload)
                if header is None:
                    continue
                self.response.append(Response(header=header, payload=payload))

    def write(self, content_name):
        # enumerate 返回枚举对象 （n, 'str')
        for i, response in enumerate(self.response):
            content, content_type = extract_content(response, content_name)
            if content and content_type:
                fname = os.path.join(OUTDIR, f'ex_{i}.{content_type}')
                print(f'Wring {fname}')
                with open(fname, 'wb') as f:
                    f.write(content)


if __name__ == '__main__':
    pfile = 'pcap.pcap'
    recapper = Recapper(pfile)
    recapper.get_response()
    recapper.write('image')