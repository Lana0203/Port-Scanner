import socket
from IPy import IP

# scan every target individually
def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning target] ' + str(target))
    for port in range (1, 500):
        scan_port(converted_ip, port)

# convert a domain to an IP address
def check_ip(ip):
    try:
        IP(ip)
        return(ip)
# if user entered an ip we will convert it to the ip format and return the value
    except ValueError:
        return socket.gethostbyname(ip)
# if user entered a domain name we will convert it to an ip address format

# return a function that allows us to receive bits to be able to work out which service is running on the specific port
def get_banner(s):
    return s.recv(1024)

# connect to the port while setting the trying time to 0.5sec for faster scanning
def scan_port(ipaddress, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ipaddress, port))
        try:
            banner = get_banner(s)
            print('[+] Open port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
    # while connecting to socket try to get banner that is decoded and stripped
        except:
            print('[+] Open port ' + str(port))
    # if we don't manage to get banner then simply print the open port
    except:
        pass
#if this is the main program then run this part of the code
if __name__ == "__main__":
    targets = input ('[+] Please enter target/s to scan (use  "," to split mutiple targets): ')
    if "," in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(" "))
    else:
        scan(targets)