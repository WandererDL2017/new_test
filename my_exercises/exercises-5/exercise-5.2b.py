from sys import argv

network = argv[1]

network = network.split('.')
one, two, three, four = network
four = four.split('/')
host, subnet = four

one = int(one)
two = int(two)
three = int(three)
host = 0
subnet = int(subnet)


bin_subnet =  "1" * subnet + "0" * (32 - subnet)
bin_subnet = list(bin_subnet)

a_str = ('').join(bin_subnet[0:8])
b_str = ('').join(bin_subnet[8:16])
c_str = ('').join(bin_subnet[16:24])
d_str = ('').join(bin_subnet[24:32])

a_int = int(a_str, 2)
b_int = int(b_str, 2)
c_int = int(c_str, 2)
d_int = int(d_str, 2)

network_template = """
                   Network:
                   {:<8} {:<8} {:<8} {:<8}
                   {:08b} {:08b} {:08b} {:08b}

                   Mask:
                   /{:<8}
                   {:<8} {:<8} {:<8} {:<8}
                   {:08b} {:08b} {:08b} {:08b}
                   """

print(network_template.format(one, two, three, host, one, two, three, host, subnet, a_int, b_int, c_int, d_int, a_int, b_int, c_int, d_int))