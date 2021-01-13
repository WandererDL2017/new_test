ipAddress = input("Введите ip-адрес в формате XXX.XXX.XXX.XXX: ")
ip = ipAddress.split('.')
firstOctet = int(ip[0])

if firstOctet in range(1,224):
    print('unicast')
elif firstOctet in range(224,240):
    print('multicast')
elif ipAddress == "255.255.255.255":
    print('local broadcast')
elif ipAddress == "0.0.0.0":
    print('unassigned')
else:
    print('unused')