import socket

ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 143, 161, 162, 433, 990, 3389, 8080, 8443]
ports_open = []

print("\n" + "*" * 70)
print(' ' * 3 + 'This program takes an IPv4 address and performs a TCP port scan.')
print(' ' * 12 + 'Enter your target (IPv4 or domain name) below.')
print("*" * 70 + '\n')


while True:
    target = input('Target: ')
    try:
        ip = socket.gethostbyname(target)
        break
    except:
        print('Please enter a valid IPv4 address or domain name.\n')

print("\n" + "*" * 70)
print('If you want to scan any specific port enter it below.\nIf you leave it blank it will scan common TCP ports.')
print("*" * 70 + '\n')

while True:
    port = input('Port to scan: ')
    if port == '':
        break
    elif port.isdigit() == False:
        print ('Please enter a decimal value / a single port at a time.\n')
        continue
    elif ports == [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 143, 161, 162, 433, 990, 3389, 8080, 8443]:
        ports = []
    port = int(port)
    ports.append(port)

print("\n" + "*" * 70)
print("Scanning: " + target)
print("*" * 70)

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((ip, port))
    if result == 0:
        ports_open.append(port)
    s.close()

print("Scan Finished!")
print("*" * 70 + '\n')


if len(ports_open) == 0:
    print('No open ports were found.\n')

elif len(ports_open) == 1:
    print('There was ' + str(len(ports_open)) + " open port.\n")
    print('Port: ' + str(ports_open[0]) + '\n')

elif len(ports_open) > 1:
    print('There were ' + str(len(ports_open)) + " open ports.\n")
    for p in ports_open:
        print('Port: ' + str(p))
    print('\n')
print("*" * 70 + "\n")

