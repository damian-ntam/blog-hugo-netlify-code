import requests
from authenticate import get_token
from pprint import pprint
import json

def main():
    dnac = "10.48.82.183"
    token = get_token(dnac)
    
    url = f"https://{dnac}/dna/intent/api/v1/"
    
    family = "Switches and Hubs"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-auth-Token": token 
    }

    device_url = url + "network-device?family=" +  family
    response =  requests.get(device_url, headers=headers, verify=False ).json()
    devices = response["response"]

    device_list = []

    # Store all device ids in a list
    for device in devices:
        device_list.append(device['id'])
    #print(device_list)

    # Pass the device list into the payload
    payload = {
        "commands": [
            "show version"
        ],
        "deviceUuids": device_list
    }

    # Call the command runner endpoint
    command_url = url + "network-device-poller/cli/read-request"
    response = requests.post(command_url, headers=headers, data=json.dumps(payload), verify=False )

    print(response.text)

if __name__ == "__main__":
   main()