import requests
from authenticate import get_token
from pprint import pprint

def main():
   dnac = "sandboxdnac2.cisco.com"
   token = get_token(dnac)
   
   url = f"https://{dnac}/dna/intent/api/v1/client-health"

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }

   querystring = { "timestamp": ""}

   response =  requests.get(url, headers=headers, params=querystring, verify=False ).json()

   scores = response['response'][0]['scoreDetail']

   d = {
      'wired' : {},
      'wireless': {}
   }
   nested_dict_wired = {}
   nested_dict_wireless = {}

   print("Overview")
   print("--------")
   for score in scores:
      if score['scoreCategory']['value'] == 'ALL':
         #print(f"Total devices - all: {score['clientCount']}")
         print('')
      
      if score['scoreCategory']['value'] == 'WIRED':
         #print(f"  Total devices - wired: {score['clientCount']}")
         values = score['scoreList']
         for value in values:
            #print(f"      {value['scoreCategory']['value']}: {value['clientCount']}")
            nested_dict_wired[value['scoreCategory']['value']] = value['clientCount']
            d['wired'] = nested_dict_wired
            
      if score['scoreCategory']['value'] == 'WIRELESS':
         #print(f"  Total devices - wireless: {score['clientCount']}")

         values = score['scoreList']
         for value in values:
            #print(f"      {value['scoreCategory']['value']}: {value['clientCount']}")
            nested_dict_wireless[value['scoreCategory']['value']] = value['clientCount']
            d['wireless'] = nested_dict_wireless
  
  
   calculatePercentageHealth(d)
   #calculatePercentageHealth1(d)

def calculatePercentageHealth(d):
   print("Percentage Health")
   print("-----------------")
   #Calculate Totals
   sum_wired = 0
   for key, value in d['wired'].items():
      sum_wired += value
   
   sum_wireless = 0
   for key, value in d['wireless'].items():
      sum_wireless += value
  
   #Calculate Percentages
   for key, value in d.items():
      if key == 'wired':
         print(f"Sum_wired: {sum_wired}")
         for k, v in value.items():
            percentage = round((v/sum_wired) * 100)
            print(f"    For {k} => {percentage}%" )
      
      if key == 'wireless':
         print(f"Sum_wireless: {sum_wireless}")
         for k, v in value.items():
            percentage = round((v/sum_wireless) * 100)
            print(f"    For {k} => {percentage}%" )
     


def calculatePercentageHealth1(d):
  # first, calculate sums for each brand
  s = {k:sum(v.values()) for k, v in d.items()}
  print("--------")
  print(s)
  print("--------")

  for k, v in d.items():
    print(k)
    for p, n in v.items():
      perc = n * 100.0 / s[k]
      print(f"  {p} {perc:0.0f}%")

if __name__ == "__main__":
   main()