'''
List the guest info
'''
import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from mongodbConnection import connect_mongo

# Load and get environment variables
load_dotenv(find_dotenv())
USER = os.environ.get("USER")
PASS = os.environ.get("PASS")
ADDRESS = os.environ.get("ADDRESS")

def main():
    # Instantiate a ISE ERS API session
    url = f'https://{USER}:{PASS}@{ADDRESS}/ers/config/guestuser'

    payload={}
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    a = response.json()
    b = a['SearchResult']['resources']
    print(a['SearchResult']['resources'])

    for res in b:
        id = res['id']
        print(res['id'])
        url2 = f'https://{USER}:{PASS}@{ADDRESS}/ers/config/guestuser/{res["id"]}'

        response1 = requests.request("GET", url2, headers=headers, data=payload, verify=False)
        res = response1.json()
        print(res)
        connect_mongo(data='GuestInfo', collection=f'{res["GuestUser"]["id"]}', content=res)  

# Execute and print the total runtime                           
if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f'\nScript complete, total runtime {end_time - start_time}')
