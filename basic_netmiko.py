####Basic Netmiko####
From netmiko import Netmiko 

Connection =Netmiko(host='191.168.101.148', port='22', username='cisco', password='cisco',device_type='cisco_ios')
Output = connection.end_command('sh ip int br')
Print(output) 
Print('Closingconnection')Connection.disconnect()
