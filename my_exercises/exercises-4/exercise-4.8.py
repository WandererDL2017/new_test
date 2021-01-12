ip = "192.168.3.1"

ip = ip.split('.')
one, two, three, four = ip

one = int(one)
two = int(two)
three = int(three)
four = int(four)

ip_template = """
              {:<8} {:<8} {:<8} {:<8}
              {:08b} {:08b} {:08b} {:08b}
              """

print(ip_template.format(one, two, three, four, one, two, three, four))