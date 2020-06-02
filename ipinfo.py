import argparse
import sys
import requests
import socket
import json
from colorama import Fore, Back, Style, init
init(autoreset=True)

parser = argparse.ArgumentParser(description='Takes a hostname and runs it against ipinfo.py', prog='ipinfo.py', usage='python3 %(prog)s [hostname]\nexample: python3 ipinfo.py google.com')
parser.add_argument("hostname", help="example: google.com")
args = parser.parse_args()


#Prints GET headers
req_ = requests.get("https://"+sys.argv[1])
print("\n"+str(req_.headers))

gethost_ = socket.gethostbyname(sys.argv[1])
hostip_ = Fore.RED + gethost_
print("The IP address of "+sys.argv[1]+" is: "+hostip_)

#ipinfo.ip against domain name
info_ = requests.get("https://ipinfo.io/"+gethost_+"/json")
resp_ = json.loads(info_.text)

loc_ = Fore.GREEN + resp_["loc"]

#print("location: " +resp_["loc"])
print("location: " +loc_)
print("region: " +resp_["region"])
print("city: " +resp_["city"])
print("country: " +resp_["country"])
print("zip code: " +resp_["postal"])
print("timezone: " +resp_["timezone"])
print("org: " +resp_["org"])
