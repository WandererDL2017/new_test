network = input('Введите сеть:(ip/mask) ')

network = network.split('.')
one, two, three, four = network
four = four.split('/')
host, subnet = four

host = int(host)
one = int(one)
two = int(two)
three = int(three)
subnet = int(subnet)


bin_subnet =  "1" * subnet + "0" * (32 - subnet)
split_subnet = bin_subnet.split(maxsplit=4)

print(split_subnet)

network_template = """
                   Network:
                   {:<8} {:<8} {:<8} {:<8}
                   {:08b} {:08b} {:08b} {:08b}

                   Mask:
                   /{:<8}
    
                   """

print(network_template.format(one, two, three, host, one, two, three, host, subnet))