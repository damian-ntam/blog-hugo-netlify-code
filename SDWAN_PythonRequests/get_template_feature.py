import requests
import json
from authenticate import login
from pprint import pprint

def get_templates():
    session = login()

    baseurl = "https://sandboxsdwan.cisco.com:8443"

    template_endpoint = "/dataservice/template/feature"
    url = f"{baseurl}{template_endpoint}"
    
    response_template = session.get(url, verify=False).json()
    #pprint(response_template)

    templates = response_template['data']

    for template in templates:
        print(f"Template with id {template['templateId']}")
        for device in template['deviceType']:
            print(f"    Associated device => {device}")

if __name__ == "__main__":
   response = get_templates()
 