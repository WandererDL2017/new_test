ipAddress = input("Введите ip-адрес в формате XXX.XXX.XXX.XXX: ")
ip = ipAddress.split('.')
octets = len(ip) == 4

for i in ip:
    octets = i.isdigit() and 0 <= i.isdigit() <= 255 and octets
    print('Неверный IPv4')
    break


if ip[0].isdigit() in range(1,224):
        print('unicast')
elif ip[0].isdigit() in range(224,240):
        print('multicast')
elif ipAddress == "255.255.255.255":
        print('local broadcast')
elif ipAddress == "0.0.0.0":
        print('unassigned')
else:
        print('unused')

