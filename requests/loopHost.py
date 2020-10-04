# !/bin/python3
# This is equivalent to /sockets/loopHost.py

import sys
import socket
import requests
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
path = '/'
host = 'http://' + target + ':' + str(port)
while True:
    response = requests.get(host + path)
    status_code = response.status_code
    if status_code == 200:
        json_res = response.json()

        if json_res['value'] == 'end' and json_res['next'] == 'end':
            break

        value = value + json_res['value']
        path = '/' + json_res['next']

print(value)
sys.exit()
