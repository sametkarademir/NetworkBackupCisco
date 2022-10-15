import os
from netmiko import ConnectHandler
from datetime import datetime

files = os.path.dirname(os.path.abspath(__file__))


with open("InventoryList.txt") as f:
    lines = f.read().splitlines()


for item in lines:
    host = item.split()


def CiscoSshConnect(address: str, username: str, password:str):
    try:
        devices = {
            'device_type': 'cisco_ios',
            'ip': address,
            'username': username,
            'password': password
        }

        response = os.system("ping " + address)
        if response == 0:
            net_connect = ConnectHandler(**devices)
            output = net_connect.send_command("show running-config")
            net_connect.disconnect()
            if output is not None:
                url = files + "/backup/"+ address + "_Sw_" + str(datetime.now())
                fl = open(url, "w")
                fl.write(output)
            else:
                return print("null")
        else:
            print("device not reachable")

    except:
        pass