from scrapli.driver.core import IOSXEDriver
from scrapli.driver.core import IOSXRDriver

devices = [{
    "host": "ios-xe-mgmt-latest.cisco.com",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "port": 8181,
    "auth_strict_key": False,
}, {
    "host": "sbx-iosxr-mgmt.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "port": 8181,
    "auth_strict_key": False,
}]

conn_XE = IOSXEDriver(**devices[0])
conn_XE.open()
responses = conn_XE.send_commands(["show version", "show ip int brief"])

for response in responses:
   print("RESPONSE")
   print("*" * 100)
   print(response.result)
conn_XE.close()


conn_XR = IOSXRDriver(**devices[1])
conn_XR.open()
responses = conn_XR.send_commands(["show version", "show ip int brief"])

for response in responses:
   print("RESPONSE")
   print("*" * 100)
   print(response.result)
conn_XR.close()