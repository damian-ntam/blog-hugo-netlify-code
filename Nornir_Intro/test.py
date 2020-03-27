from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command, netmiko_send_config
from nornir.plugins.tasks.networking import napalm_get, napalm_cli
from nornir.plugins.functions.text import print_result
from nornir.core.filter import F


nr = InitNornir('nornir_config.yml')

print(nr.config.core.num_workers)
r1 = nr.inventory.hosts['DEV01']
print(r1.groups)
print(r1.username)


# result = nr.run(netmiko_send_command, command_string="show ip int br")#
# print_result(result)

#result = nr.run(netmiko_send_command, command_string="show version")#
#print_result(result)

#result = nr.run(napalm_get, getters=['get_interfaces'])
#print_result(result)

#r2 = nr.filter(name="DEV02")

#result = r2.run(netmiko_send_command, command_string="show ip int br")#
#print_result(result)

#result = nr.run(task=napalm_get, getters=["interfaces"])
#print_result(result)

#result = nr.run(napalm_cli, commands=['show version', 'show interface brief'])
#print_result(result)

#result = nr.run(netmiko_send_command, commands=['show version', 'show interface brief'])
#print_result(result)



description = 'Description set with Nornir'

description_config = [
    "interface GigabitEthernet3",
    f"description {description}",
]
   
result = nr.run(netmiko_send_config, config_commands=description_config)
print_result(result)


