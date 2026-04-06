import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")


try:
    n = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=3d3c5827a336fedf464499b3ba9ec9c7d8177f3322e4e11000671e27688950ed")
    object = response.json()
    price_btc = float(object["data"]["priceUsd"])
    amount = price_btc * n
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit("API Error")
