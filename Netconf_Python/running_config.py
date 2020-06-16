from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom

router = {
   'host': 'ios-xe-mgmt-latest.cisco.com',
   'port': '10000',
   'username': 'developer',
   'password': 'C1sco12345'
}

m = manager.connect(**router, device_params={'name':'iosxe'}, hostkey_verify=False)

running_config = m.get_config('running')
print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

m.close_session()


