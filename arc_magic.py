#! /opt/local/bin/python
-*- coding: ascii -*-

import sys
import zlib
import magic

def dec_member(in_file, buffer):
    CHUNKSIZE = 1024
    d = zlib.decompressobj(16 + zlib.MAX_WBITS)
    rec = ''
    nr_bytes = len(buffer)
    while not d.unused_data:
        tmp = in_file.read(CHUNKSIZE)
        nr_bytes += len(tmp)
        buffer = buffer + d.unconsumed_tail + tmp
        if len(buffer) == 0: break
        rec += d.decompress(buffer)
        buffer = ''
    rec += d.flush()
    nr_bytes -= len(d.unused_data)
    return (rec, d.unused_data, nr_bytes)

def record_iterator(f):
    buffer = ''
    first = True
    while first or buffer != '':
        first = False
        (rec, buffer, nr_bytes) = dec_member(f, buffer)
        yield (rec, nr_bytes)

class Filedesc: pass

class DNS_rec: pass

class HTTP_rec:
    def __init__(self, url, ip_addr, ts, mime_type, size, payload):
        # TODO surely there is better than that to create members
        self.url = url
        self.ip_addr = ip_addr
        self.ts = ts
        self.mime_type = mime_type
        self.size = size
        self.payload = payload

def parse_http_rec(rec):
    (i, j) = (0, rec.index('\n'))
    [url, ip_addr, ts, mime_type, size] = rec[i:j].split(' ')
    header_end = rec.index('\r\n\r\n')
    return HTTP_rec(
        url, ip_addr, ts, mime_type, size, rec[header_end + len('\r\n\r\n'):])

def parse(rec):
    type = rec[:rec.index(':')]
    if type == 'filedesc': return Filedesc()
    elif type == 'dns': return DNS_rec()
    elif type == 'http': return parse_http_rec(rec)
    else: raise Exception('Unknown record type: ' + type)

in_f = open(sys.argv[1], 'rb')
ms = magic.open(magic.MAGIC_NONE)
ms.load()
for (rec, nr_bytes) in record_iterator(in_f):
    pr = parse(rec)
    if isinstance(pr, HTTP_rec):
        print pr.url, pr.ts, ms.buffer(pr.payload)
in_f.close()
