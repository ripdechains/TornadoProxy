import sys
import time
import os
import requests as r
import json
import random


url="http://localhost:4050/"
def API_not_available():
    try:
        status_code=r.get(url).status_code
        status_code==200
    except:
           return True
           
if API_not_available():
   print("Can't access API. Make sure that your Mysterium Node is running and successfully registered.\n\nHow to run a node on Windows: https://docs.mysterium.network/for-node-runners/mysterium-node-windows-installer \n\nHow to run a node on Linux: https://docs.mysterium.network/for-node-runners/linux-guide\n\n")
   print("Exiting...")
   sys.exit()
else:
     print("Loading providers...")
     
     global all_providers
     global EU_providers
     global NA_providers
     global SA_providers
     global AS_providers
     global OC_providers
     global AF_providers
     
     all_providers=[]
     EU_providers=[]
     NA_providers=[]
     SA_providers=[]
     AS_providers=[]
     OC_providers=[]
     AF_providers=[]
     
     providers=r.get(url+'proposals').json()
     for p in range(len(providers["proposals"])):
         provider_id=providers["proposals"][p]["provider_id"]
         all_providers.append(provider_id)
         ZONE=providers["proposals"][p]["location"]["continent"]
         if ZONE=="EU":
            EU_providers.append(provider_id)
         elif ZONE=="NA":
            NA_providers.append(provider_id)
         elif ZONE=="SA":
            SA_providers.append(provider_id)
         elif ZONE=="AS":
            AS_providers.append(provider_id)
         elif ZONE=="OC":
            OC_providers.append(provider_id)
         elif ZONE=="AF":
            AF_providers.append(provider_id)
     print("---------------")      
     print("Total:",len(all_providers), "\nEurope:",len(EU_providers),"\nNorth America:",len(NA_providers),"\nSouth America:",len(SA_providers),"\nAsia:",len(AS_providers),"\nOceania:",len(OC_providers),"\nAfrica:",len(AF_providers))
     print("---------------")
     print("\n\n")
if not os.path.exists("config.json"):
   print("No configuration file was found. Exiting ...")
   sys.exit()
else:
     print("Loading configuration...")
     print("\n\n")
     try:
         config=open("config.json")
         config=json.load(config)
         global config_ZONE
         global config_ACTION
         
         config_ZONE=config["zone"]
         config_ACTION=config["action"]
     except:
            print("Cannot load configuration file. It may contains errors or be corrupted. Exiting...")
            sys.exit()
     finally:
             if config_ZONE=="any" or config_ZONE=="EU" or config_ZONE=="NA" or config_ZONE=="SA" or config_ZONE=="AS" or config_ZONE=="OC" or config_ZONE=="AF" and os.path.exists(config_ACTION):
                    pass
             else:
                  print("Please check your configuration.\nAvailable zone key values: any,EU,NA,SA,AS,OC,AF\naction key must contains a valid file path")
                  
global cons_id
cons_id=input("Type your consumer ID (if wrong, non-existent or not yours will cause error):\n\n")
def run_tornado():
    r.delete(url+"connection")
    global random_provider
    if config_ZONE=="EU":
       random_provider=random.choice(EU_providers)
    elif config_ZONE=="NA":
         random_provider=random.choice(NA_providers)   
    elif config_ZONE=="SA":
         random_provider=random.choice(SA_providers)
    elif config_ZONE=="AS":
         random_provider=random.choice(AS_providers)  
    elif config_ZONE=="OC":
         random_provider=random.choice(OC_providers) 
    elif config_ZONE=="AF":
         random_provider=random.choice(AF_providers)
    elif config_ZONE=="any":
         random_provider=random.choice(all_providers)
    data={}
    data["provider_id"]=random_provider
    data["consumer_id"]=cons_id

    headers = {"Content-Type": "application/json"}
    x=r.put(url+"connection", data=json.dumps(data),headers=headers)

    res=x.json()
    
    
    if res["status"]=="Connected":
       get_ip=r.get(url+"connection/ip").json()
       get_loc=r.get(url+"connection/proxy/location").json()
       print("Connection started...")
       time.sleep(1)
       print("Your public IP has changed:",get_ip["ip"],"Country:",get_loc["country"],"City:",get_loc["city"])
       print("\n")
      
    else:
         print(res["error"]["message"])
         sys.exit()
    print("Executing",config_ACTION)


                  
while True:
      run_tornado()
      os.system(config_ACTION)
      
     
     
                  

             
     
             
     
     
     




    
