# TornadoProxy 🌪️ (powered by Mysterium Network's Tequilapi)

 Join Discord: https://discord.com/channels/1014477172259430411/


# Requisites:
-A registered and running Mysterium Node, see https://docs.mysterium.network/for-node-runners/intros-mysterium-node

-Python>=3.8

# Downlaoding and running TornadoProxy:
```
git clone https://github.com/ripdechains/TornadoProxy.git
cd TornadoProxy
python3 start_tornado.py
```

# How to use :

You will find 4 files (```start_tornado.py```, ```config.json``` , ```run.bat``` and ```run.sh```)
 ```run.bat``` and ```run.sh``` are essentially the same thing, but ```run.bat``` is what you need if you are on Windows and ```run.sh``` is what you need if you are on Linux. So if for example you are on Windows ,just remove ```run.sh``` and just keep ```run.bat``` and viceversa. if you are on Windows then you will also need to modify your config.json by specifying ```run.bat``` instead of ```./run.sh```
 
Tornado chooses a random proxy to connect to, first will connect to it, changing your public IP address, then executes the code contained within ```run.sh``` (or run.bat) , which you can modify as you wish, when the code has finished running, it will switch the provider with another random one and the code will run again, until you stop it. If you do not want code to be executed at every switch: by default, inside run.sh you will find ```sleep 30```, this simply means that nothing will be executed but only 30 seconds will pass from one provider change to another. You can change 30 to the number of seconds you want to pass for every switch.
 You will find a configuration file called config.json. It must always remain in the same folder where ```start_tornado.py``` resides. Within it you can change the "zone" key by inserting: ```any``` if you want IP addresses from any part of the world to be chosen randomly, or restrict only to a certain continent using the tickers ```EU```, ```NA```,```SA```, ```AS```, ```OC```, ```AF``` (Europe, North America, South America, Asia, Oceania, Africa), also in the "action" key you can change the path of the file to be executed instead of ./run.sh (which is default)

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





If you found this software useful please consider a donation:

**Polygon / Myst: 0x45320b5B2a8f6073f4a92FFDF149861aBade4B4b**

**Bitcoin: 1LjyKgstk1dQsSU6njFd4RfGw3C9JBtVuG**

**Solana: 6RX2ADdcNWZfaUfuGeHg86AYAoMuLF45Lbgfu3oNGh9i**

**Monero: 82qjYLZj6XeTGjeUNm9AQVB78hVGStZd8YU1UKuvWz8QKAzFWZpBpEQFho3jrvUCNQPSqC9nYeEN3b7FQ5REPffNSA2WSDH**

**Litecoin: ltc1q4ft4ltjnyt8auqq4m5u7raatftu6mt5snst493**

**Ethereum: 0xF3A0246690947669A0bf68147Ba82AC8de576a56**

Thank you :-)
