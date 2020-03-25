from netmiko import ConnectHandler

devices = [{
    "device_type": "cisco_xr",
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "8181",
}]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show version")
    net_connect.disconnect()
    result = output.find('uptime is')
    begin = int(result)
    end = begin + 39
    print(device['ip'] + " => " + output[int(begin):int(end)])
    