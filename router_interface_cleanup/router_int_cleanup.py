from netmiko import ConnectHandler
import getpass

def get_int_list(filepath):
    with open(filepath) as f:
        content = f.readlines()
        return [line.split()[0] for line in content][1:]

get_int_list('router_interface_cleanup\interface_description.txt')


def get_device_list():
    devices = open_device_file()
    device_list = list()
    Login= getpass.getpass("Password : ")
    Enable= getpass.getpass("Secret : ")    
    for ip in devices:
        cisco_device = {
            'device_type': 'cisco_ios_telnet',
            'ip': ip,
            'username': '',
            'password': Login,
            'secret': Enable,
            }
        device_list.append(cisco_device)
    
    return device_list

def open_device_file():
    with open("router_interface_cleanup/routers.txt") as f:
        devices = f.read().splitlines()
    return devices



def get_int_desc():
    for device in get_device_list() :
    #print('Connecting to ' + device['ip'])
        try:
            connection = ConnectHandler(**device)
            connection.enable()
            find_hostname = connection.find_prompt()
            hostname = find_hostname[:-1]
            output = connection.send_command("show interface description")
            f = open("recent_config.txt", "w")
            f.write(hostname)
            f.write(output)
            f.close()
        
            with open(hostname + '.txt', 'r') as f2:
                with open('recent_config.txt', 'r') as f1:
                    same = set(f1).difference(f2)
            same.discard('\n')
            with open('new_config.txt', 'a') as f3:
                print(hostname)
                for line in same:
                    if 'description' in line:
                        print(line)
        
            with open('recent_config.txt') as f:
                with open(hostname + '.txt', "w") as f1:
                    for line in f:
                        f1.write(line)
                                       
        except (NameError, OSError, ValueError) as e:
            print ("Unable to connect!:", e) 
        
    
#connection.disconnect()

    same.discard('\n')

    with open('recent_config.txt') as f:
        with open(hostname + '.txt', "w") as f1:
            for line in f:
                f1.write(line)

get_int_desc()

