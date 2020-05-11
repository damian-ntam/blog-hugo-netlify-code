import requests
import json
from authenticate import login
from pprint import pprint

def build_template():
    session = login()

    #baseurl = "https://sandboxsdwan.cisco.com:8443"
    baseurl = "https://10.10.20.90:8443"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
    "templateName": "Basic_template",
    "templateDescription": "Collection of default templates",
    "deviceType": "vsmart",
    "configType": "template",
    "factoryDefault": False,
    "policyId": "",
    "featureTemplateUidRange": [],
    "generalTemplates": [
        {
            "templateId": "476b52d0-3196-4625-82be-1deb124a5199",
            "templateType": "aaa"
        },
        {
            "templateId": "2767ed11-d403-42d4-9dcc-f5471e2a2e3b",
            "templateType": "omp-vsmart"
        },
        {
            "templateId": "1918ba5d-e91d-4682-b889-71fd5fd27765",
            "templateType": "security-vsmart"
        },
        {
            "templateId": "ab4beafa-bfa4-44b3-9436-9bb62221420e",
            "templateType": "system-vsmart"
        },
        {
            "templateId": "5202f0a4-86c5-40af-979d-492b9e11a90a",
            "templateType": "vpn-vsmart"
        },
        {
            "templateId": "bf3fcac8-8ab3-46a3-9ab5-c0d3e6107826",
            "templateType": "vpn-vsmart"
        }
    ]
}

    # Get all certificates
    template_endpoint = "/dataservice/template/device/feature"
    url = f"{baseurl}{template_endpoint}"
    response_template = session.get(url, headers=headers, data=json.dumps(payload), verify=False).json()

    pprint(response_template)


  
    
if __name__ == "__main__":
   response = build_template()
