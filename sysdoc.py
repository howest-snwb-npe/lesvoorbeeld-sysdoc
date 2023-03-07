# Het script zal de volgende zaken opvragen en bijhouden:
# hostname
# OS
# ip-adres

hostname = input("Geef de hostname: ")
os = input("Geef het OS: ")
ip = input("Geef het ip-adres: ")

print(f"{hostname:20} {os:15} {ip:30}")

#{ "key": "value" }
system = {"hostname": hostname, "os": os, "ip": ip}
print(system)