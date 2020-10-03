# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# !/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777


def format1(v1):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Connection HOST: {v1}')  # Press Ctrl+F8 to toggle the breakpoint.


def format2(v2):
    print('Connection PORT: {}'.format(v2))


format1(HOST)
format2(PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Press the green button in the gutter to run the script.
'''
if __name__ == '__main__':
    print_hi('PyCharm')
    '''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
