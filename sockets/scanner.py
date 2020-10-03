# !/bin/python3

import sys
import socket
from datetime import datetime

# Define the target
if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4, it's verbose
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <IP>")

# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # return an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
