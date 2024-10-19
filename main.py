import os
from pick import pick
import subprocess
import sys

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def Main():
    clear_terminal()

    title = 'Please choose your DNS Server: '
    options = ['Google', 'Cloudflare','Custom','Exit']

    option, index = pick(options, title, indicator='=>', default_index=0)

    if index == 0:  # Google DNS
        if os.name == "nt":
            adapter = "Wi-Fi"  
            dns_servers = ["8.8.8.8", "8.8.4.4"]

            try:
                # İlk DNS sunucusunu ekleme
                command = f'netsh interface ipv4 set dns "{adapter}" static {dns_servers[0]}'
                subprocess.run(command, shell=True, check=True)

                # İkinci DNS sunucusunu ekleme
                command = f'netsh interface ipv4 add dnsservers "{adapter}" address={dns_servers[1]} index=2'
                subprocess.run(command, shell=True, check=True)

                print(f"DNS settings changed successfully: {dns_servers}")
            except subprocess.CalledProcessError as e:
                print(f"ERROR: {e}")
        else:  
            dns_servers = ["8.8.8.8", "8.8.4.4"]
            try:
                with open('/etc/resolv.conf', 'w') as f:
                    for server in dns_servers:
                        f.write(f"nameserver {server}\n")
                print(f"DNS settings changed successfully: {dns_servers}")
            except PermissionError:
                print("You need administrator (root) privileges to perform this operation.")
            except Exception as e:
                print(f"ERROR: {e}")


    elif index == 1:
        if os.name == "nt":
            adapter = "Wi-Fi"  
            dns_servers = ["1.1.1.1", "1.0.0.1"]

            try:
                # İlk DNS sunucusunu ekleme
                command = f'netsh interface ipv4 set dns "{adapter}" static {dns_servers[0]}'
                subprocess.run(command, shell=True, check=True)

                # İkinci DNS sunucusunu ekleme
                command = f'netsh interface ipv4 add dnsservers "{adapter}" address={dns_servers[1]} index=2'
                subprocess.run(command, shell=True, check=True)

                print(f"DNS settings changed successfully: {dns_servers}")
            except subprocess.CalledProcessError as e:
                print(f"ERROR: {e}")
        else:  
            dns_servers = ["1.1.1.1", "1.0.0.1"]
            try:
                with open('/etc/resolv.conf', 'w') as f:
                    for server in dns_servers:
                        f.write(f"nameserver {server}\n")
                print(f"DNS settings changed successfully: {dns_servers}")
            except PermissionError:
                print("You need administrator (root) privileges to perform this operation.")
            except Exception as e:
                print(f"ERROR: {e}")
    elif index == 2:
        if os.name == "nt":
            adapter = "Wi-Fi"
            dns1 = input("Enter 1. Custom DNS : ") 
            dns2 = input("Enter 2. Custom DNS : ")
            try:
                # İlk DNS sunucusunu ekleme
                command = f'netsh interface ipv4 set dns "{adapter}" static {dns1}'
                subprocess.run(command, shell=True, check=True)

                # İkinci DNS sunucusunu ekleme
                command = f'netsh interface ipv4 add dnsservers "{adapter}" address={dns2} index=2'
                subprocess.run(command, shell=True, check=True)

                print(f"DNS settings changed successfully")
            except subprocess.CalledProcessError as e:
                print(f"ERROR: {e}")

        else:  
            dns_servers = []
            dns1 = input("Enter 1. Custom DNS : ") 
            dns2 = input("Enter 2. Custom DNS : ")

            dns_servers.append(dns1)
            dns_servers.append(dns2)
            try:
                with open('/etc/resolv.conf', 'w') as f:
                    for server in dns_servers:
                        f.write(f"nameserver {server}\n")
                print(f"DNS settings changed successfully: {dns_servers}")
            except PermissionError:
                print("You need administrator (root) privileges to perform this operation.")
            except Exception as e:
                print(f"ERROR: {e}")


    elif index == 3:
        print("Exiting The Program...")
        sys.exit(0)



if __name__ == "__main__":
    Main()
