#!/usr/bin/env python3

import sys
import socket
import nmap

print("Arguments: ")

count = 0

for i in sys.argv:
    print("Argument ",count," : ",i)
    count += 1
    
def scan(gmask,addr_start,addr_end):
    nm = nmap.PortScanner()
    while addr_start != (addr_end+1):
        current_address = str(gmask) + '.' + str(addr_start)
        nm.scan(current_address,'22-443')
        print(nm.scaninfo())
        addr_start += 1
        
        
scan('192.168.2',1,255)

usage = "\nCorrect usage: ipscan.py [gateway] [start of IP range] [end of IP range]"




if __name__ == "__main__":
    if len(sys.argv) > 4:
        print(usage)
    gmask = str(sys.argv[1])
    addr_start = int(sys.argv[2])
    addr_end = int(sys.argv[3])
    
    scan(gmask,addr_start,addr_end)