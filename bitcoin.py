#imports the relevant libraries
import sys
import requests
import json

#returns relevant errors if user enters a wrong argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

else:
    try:
     bitcoin = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") #fetches up-to-date dollar-bitcoin exchange rate
r = response.json() 
#print(json.dumps(r, indent = 3))
rate = r["bpi"]["USD"]["rate_float"]
cost = rate * bitcoin #conversion
print(f"${cost:,.4f}")
