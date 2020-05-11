from netmiko import ConnectHandler

devices = [{
    "device_type": "cisco_xr",
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "8181",
}, {
    "device_type": "cisco_xe",
    "ip": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": "8181",
}]

for device in devices:
    #net_connect = ConnectHandler(**device)
   net_connect = ConnectHandler(
      device_type = device['device_type'],
      ip = device['ip'],
      username = device['username'],
      password = device['password'],
      port = device['port']
   )
   output = net_connect.send_command("show ip int brief")
   net_connect.disconnect()
   print("*"*100)
   print(output)
   print("-"*100)