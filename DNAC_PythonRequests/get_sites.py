import requests
from authenticate import get_token
from pprint import pprint

def main():
   token = get_token()

   dnac = "sandboxdnac2.cisco.com"
   url = f"https://{dnac}/dna/intent/api/v1/site"

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }

   response =  requests.get(url, headers=headers, verify=False ).json()

   #sites = response["response"]
   #pprint(sites)

sites = ['Parent/SiteA',
'Parent/SiteB',
'Parent/SiteC',
'Parent/SiteD',
'Parent/SiteD/xyz',
'Parent/SiteE',
'Parent/SiteD/xyz/Site8',
'Parent/SiteE/def',
'Parent/SiteF/Site3',
'Parent/SiteF',
'Parent/SiteF/Site4',
'Parent/SiteF/Site5',
'Parent/SiteF/Site10',
'Parent/SiteP',
'Parent/SiteP/Site68']

sites.sort()
for line in sites:
   print('   '*line.count('/') + line.split('/')[-1])

 

#for site in sites:
   #if 'parentId' in site.keys():
      #print(f"{site['siteNameHierarchy']}")


if __name__ == "__main__":
   main()