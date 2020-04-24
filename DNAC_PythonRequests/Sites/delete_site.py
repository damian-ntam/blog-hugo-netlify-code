import requests
from authenticate import get_token
import json, time

def main():
   #dnac = "sandboxdnac2.cisco.com"
   dnac = "10.48.82.183"

   token = get_token(dnac)

   url = f"https://{dnac}"

   site_name = "TESTSITE"
   building_name = "TESTBUILDING"
   floor_name = "TESTFLOOR-1"
   mydict = {}

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }  


   building_url = f"/dna/intent/api/v1/site?name=Global/{site_name}/{building_name}"
   response_building =  requests.get(url + building_url, headers=headers, verify=False ).json()
   mydict['building'] = response_building['response'][0]['id']

   floor_url = f"/dna/intent/api/v1/site?name=Global/{site_name}/{building_name}/{floor_name}"
   response_floor =  requests.get(url + floor_url, headers=headers, verify=False ).json()
   mydict['floor'] = response_floor['response'][0]['id']

   site_url = f"/dna/intent/api/v1/site?name=Global/{site_name}"
   response_site =  requests.get(url + site_url, headers=headers, verify=False ).json()
   mydict['site'] = response_site['response'][0]['id']

   print(mydict)

   site_url = url + "/dna/intent/api/v1/site/"
   for k, v in mydict.items():
      response =  requests.delete(site_url + v, headers=headers, verify=False ).json()

if __name__ == "__main__":
   main()