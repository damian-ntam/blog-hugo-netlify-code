from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom

router = {
   'ip': 'ios-xe-mgmt-latest.cisco.com',
   'port': '10000',
   'username': 'developer',
   'password': 'C1sco12345'
}

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

netconf_filter = """
<filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
         <name>GigabitEthernet3</name>
      </interface>
   </interfaces>
</filter>
"""

running_config = m.get_config("running", netconf_filter)

running_config_xml = xmltodict.parse(running_config.xml)["rpc-reply"]["data"]
#pprint(running_config_xml["interfaces"]["interface"])


print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())