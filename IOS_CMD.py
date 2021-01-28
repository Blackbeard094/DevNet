import os
from netmiko import ConnectHandler


platform ='cisco_ios'
host = 'csr1'
host2 = 'csr2'
username = 'admin'
password = 'admin'

def IOSXE_WR():

    print('Connecting to ' + host)
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    print('Connecting to ' + host1)
    device2 = ConnectHandler(device_type=platform, ip=host2, username=username, password=password)    

    output = device.send_command('wr mem')
    print('Writing memory to' + host)

    output2 = device2.send_command('wr mem')
    print('Writing memory to ' + host1)

    output = device.send_command('sh run')
    print('Backing up Configuration' + host)
    out_file = open('csr1.cfg', 'w')
    out_file.write(output)
    print('Writing Configuration to file')
    out_file.close()

    output2 = device2.send_command('sh run')
    print('Backing up CSR2 Configuration')
    out_file = open('csr2.cfg', 'w')
    out_file.write(output2)
    print('Writing Configuration to file')
    out_file.close()

    print('Disconnecting from devices')
    device.disconnect()
    device2.disconnect()

    