# TornadoProxy (powered by Mysterium Network's Tequilapi)

Scrape the Web easy with TornadoProxy 🌪️
DISCORD: https://discord.com/channels/614079733663006750/614079733663006752

Prerequisites:
-To be able to use TornadoProxy you must first have successfully installed and registered a Mysterium Node, see https://docs.mysterium.network/for-node-runners/intros-mysterium-node

-Python>=3.8

# Downlaoding and running TornadoProxy:
```
git clone https://github.com/ripdechains/TornadoProxy.git
cd TornadoProxy
python3 start_tornado.py
```
# Stopping / Disconnect from the proxy:
IMPORTANT: Even when you have closed the terminal window you will still be connected to the last provider used. To disconnect completely you have two options:

with cURL:
```curl -X DELETE http://localhost:4050/connection```

or with Python:
```
import requests
requests.delete ("http://localhost:4050/connection")
```
Remember to disconnect from the provider after each use so as not to continue to overpay for it!


# How it works:

The program consists of 3 files that must remain in the same directory (start_tornado.py, config.json and run.sh)
Tornado chooses a random proxy pto connect to, will change your public IP address, and executes the code contained within "run.sh", which you can modify as you wish, when the code has finished running, it will change the address again IP with another random one and the code will run again, until you stop it. You will find a configuration file called config.json. It must always remain in the same folder where start_tornado.py resides. Within it you can change the "zone" key by inserting: "any" if you want IP addresses from any part of the world to be chosen randomly, or restrict only to a certain continent using the tickers EU, NA, SA, AS, OC, AF (Europe, North America, South America, Asia, Oceania, Africa), also in the "action" key you can change the path of the file to be executed instead of ./ run.sh (which is default)


If you found this software useful please consider a donation:

**Polygon / Myst: 0x45320b5B2a8f6073f4a92FFDF149861aBade4B4b**

**Bitcoin: 1LjyKgstk1dQsSU6njFd4RfGw3C9JBtVuG**

**Monero: 82qjYLZj6XeTGjeUNm9AQVB78hVGStZd8YU1UKuvWz8QKAzFWZpBpEQFho3jrvUCNQPSqC9nYeEN3b7FQ5REPffNSA2WSDH**

**Litecoin: ltc1q4ft4ltjnyt8auqq4m5u7raatftu6mt5snst493**

**Ethereum: 0xF3A0246690947669A0bf68147Ba82AC8de576a56**

Thank you :-)
