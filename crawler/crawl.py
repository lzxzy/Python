#!/usr/bin/env python3.4
from selectors import DefaultSelector,EVENT_WRITE
import argparse
import asyncio
import logging
import sys

selector = DefaultSelector()


sock = socket.socket()
sock.setblocking(False)
try:
	sock.connerct(('zhihu.com/',80))
except BlockingIOError:
	pass

def connected():
	selector.unregister(sock.fileno())
	print('connected!')

selector.register(sock.fileno(),EVENT_WRITE,connected)

def loop():
	while  True:
		events = selector.select()
		for event_key,event_mask in events:
			callback = event_key.data
			callback()
request = 'GET {} HTTP/1.0\r\nHost: zhihu.com\r\n\r\n'.format(url)
encoded = request.encoded('ascii')

while True:
	try:
		sock.send(encoded)
		break #Done.
	except OSError as e:
		pass
print('sent')