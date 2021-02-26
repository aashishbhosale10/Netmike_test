from netmiko import 

ConnectHandlercisco_device = {              
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

output = connection.send_command('sh run')
print(output)
print(connection.check_config_mode())
p
rint('Closing connection')
connection.disconnect()
