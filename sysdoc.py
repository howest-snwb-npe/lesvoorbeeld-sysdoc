# Het script zal de volgende zaken opvragen en bijhouden:
# hostname
# OS
# ip-adres

import ipaddress

def ask_ip():
    while True:
        ip = input("Geef het ip-adres: ")
        try:
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            print("Dit is geen geldig ip")


# lijst om de dictionaries in te bewaren
systems = []

while True:
    hostname = input('Geef de hostname of "end" om te stoppen: ')
    if hostname == "end":
        break
    os = input("Geef het OS: ")
    ip = ask_ip()

    print(f"{hostname:20} {os:15} {ip:30}")

    #{ "key": "value" }
    system = {"hostname": hostname, "os": os, "ip": ip}
    #print(system)
    systems.append(system)
#print(systems)

print(f"{'hostname':20} | {'os':15} | {'ip':30}")
print('-'*65)
for system in systems:
    print(f'{system["hostname"]:20} | {system["os"]:15} | {system["ip"]:30}')