import os
import ipaddress


def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def request_ip():
    clear_screen()
    ip = input("Enter an IP address or 'q' to quit: ")
    while ip != 'q':
        is_valid_ip(ip)
        ip = input("Enter an IP address or 'q' to quit: ")
    print("Exiting...")
    exit(0)
    

def is_valid_ip(ip):
    try:
        print(f"{ipaddress.ip_address(ip)} is a valid IP address")
        return True
    except ValueError:
        print(f"{ip} is an invalid IP address")
        return False
        

if __name__ == "__main__":   
    request_ip()