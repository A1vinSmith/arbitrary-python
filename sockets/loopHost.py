# !/bin/python3

import sys
import socket
import json
from datetime import datetime

# Define the target
if len(sys.argv) == 3:
    try:
        target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4, it's verbose
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    try:
        port = int(sys.argv[2])
    except ValueError:
        print("IP should be integer")
        sys.exit()
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 loopHost.py <IP> <PORT>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

value = ''
suffix = '/'
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))

    # Send get request to server
    getRequest = f"GET {suffix} HTTP/1.0\r\nHost: {target}\r\n\r\n"
    s.send(getRequest.encode('utf8'))

    # Retrieve data from get request
    res = str(s.recv(4096), 'utf-8')  # print(s.recv(4096).decode("utf8"))
    res_lines = res.splitlines()
    last_line = res_lines[-1]
    pair = json.loads(last_line)
    if pair['value'] == 'end' and pair['next'] == 'end':
        break
    value = value + pair['value']
    suffix = '/' + pair['next']
    s.close()

print(value)
s.close()
sys.exit()
