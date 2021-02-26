####Sending Commands from file####

from netmiko import ConnectHandler

cisco_device = {              
'device_type' : 'cisco_ios',              
'host' : '192.168.101.148',             
'username' : 'cisco',             
'port' : 22,             
'secret' : 'cisco',             
'verbose' : 'True'             
}

connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()
print(prompt)
if  '>' in prompt:        

connection.enable()
print('Entering the enable mode...')

connection.enable()
print(Sending commands from file)
output = connection.send_config_from_file('ospf.txt')
print(output)
print('Closing connection')connection.disconnect()
