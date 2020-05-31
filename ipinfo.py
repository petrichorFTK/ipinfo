import sys
import requests
import socket
import json
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Print help if user messed up - doesn't work ironically
if len(sys.argv) < 2:
	print("Usage: " + sys.argv[0] + "<curl>")
	sys.exit(1)

#Prints GET headers, currently commented out
req = requests.get("https://"+sys.argv[1])
#print("\n"+str(req.headers))

gethost_ = socket.gethostbyname(sys.argv[1])
hostip_ = Fore.RED + gethost_
print ("The IP address of "+sys.argv[1]+" is: " + hostip_)

#ipinfo.io on domain name
req_two = requests.get("https://ipinfo.io/"+gethost_+"/json")
resp_ = json.loads(req_two.text)

print("location: " +resp_["loc"])
print("region: " +resp_["region"])
print("city: " +resp_["city"])
print("country: " +resp_["country"])
print("zip code: " +resp_["postal"])
print("timezone: " +resp_["timezone"])
print("org: " +resp_["org"])

#To Do -  can I push this location into Google Maps and have the browser
#show me where this location is?