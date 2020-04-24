import requests
from authenticate import get_token
from pprint import pprint
import json, time


def main():
   #dnac = "sandboxdnac2.cisco.com"
   dnac = "10.48.82.183"

   token = get_token(dnac)

   #url = f"https://{dnac}/dna/intent/api/v1/global-credential?credentialSubType=CLI"
   url = f"https://{dnac}"

   cred_url = "/api/v1/global-credential"
   credtype = "CLI"

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }

   # Part 1: Get Credentials to run the discovery
   cred_list = []
   response =  requests.get(url + cred_url, params={"credentialSubType": credtype}, headers=headers, verify=False ).json()
   cred_list.append(response["response"][0]["id"])
   #print(cred_list)

   with open("templates/discovery.json", "r") as file:
      discovery = json.load(file)
      
      # In the JSON body, there should also be a globalCredentialIdList key. This is not in the template as it depends on the above
      # action 
   discovery["globalCredentialIdList"] = cred_list
   #print(discovery)

 
   # Part 2: Run the discovery
   discover_url = f"https://{dnac}/api/v1/discovery"
   response_discovery =  requests.post(discover_url, data=json.dumps(discovery), headers=headers, verify=False ).json()
   task_url = response_discovery['response']['url']
   print(f"taskUrl => {task_url}")
   print(f"taskId => {response_discovery['response']['taskId']}")


   # Check the task
   task = waitTask(url, task_url )
   discoverId = task['response']['progress']
   print(f"DiscoverID: {discoverId}")
   discover_url = f"https://{dnac}/api/v1/discovery/{discoverId}"

   while True:
      response =  requests.get(discover_url, headers=headers, verify=False ).json()
      
      if response['response']['discoveryCondition'] == "Complete":
         print(f"Discovery with id {discoverId} completed successfully")
         print(f"Discovery found {response['response']['numDevices']} devices") 
         break
      
   time.sleep(10)
 
def waitTask(url, task_url):
   dnac = "10.48.82.183"
   token = get_token(dnac)
   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }
   for i in range(10):
      print("Starting for loop " + str(i))
      time.sleep(1)
      response_task =  requests.get(url + task_url, headers=headers, verify=False ).json()
      print(response_task)
      if response_task['response']['isError']:
         print("Error")
      if "endTime" in response_task['response']:
         print(response_task['response']['progress'])
         return response_task

if __name__ == "__main__":
   main()