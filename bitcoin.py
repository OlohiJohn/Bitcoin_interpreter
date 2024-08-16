import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

else:
    try:
     bitcoin = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r = response.json()
#print(json.dumps(r, indent = 3))
rate = r["bpi"]["USD"]["rate_float"]
cost = rate * bitcoin
print(f"${cost:,.4f}")
