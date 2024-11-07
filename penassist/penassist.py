import sys
import nmap #pip install python-nmap for this to work 
import ipaddress
import socket

def main(args):

    if (("-u" in sys.argv) and "--create-config" not in sys.argv):   # If user is creating config they can set ip there
        ip_str = 127.000 # Need to take this from the user message in chat 
        target_ip = ipaddress.ip_address(ip_str)
    else: 
        SystemError("IP has not be set, use flag -u to set a target IP")

    if "--create-config" in sys.argv:
        createConfig() 
    elif "--full-scan" in sys.argv:
        fullScan()
    elif "--quick-scan" in sys.argv: 
        quickScan() 
        
    


def quickScan(target_ip):      # Abreviated scan of system only
    print(f"Performing quick scan of {target_ip}")
    ports = 1 # WIP
    nm = nmap.PortScanner()
    nm.scan({target_ip}, ports)

    # Work in progress


def fullScan ():    # Full scan of system
    print("Performing full scan of system")
    # Work in Progress

def createConfig():
    print("creating a new configuration")

if __name__ == "__main__":
    main(sys.argv)