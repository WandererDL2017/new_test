mac = "AAAA:BBBB:CCCC"
mac = mac.split(':')

a, b, c = mac
a = int(a, 16)
b = int(b, 16)
c = int(c, 16)

print('{:b}{:b}{:b}'.format(a, b, c))

