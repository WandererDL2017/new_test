config = "switchport trunk allowed vlan 1,3,10,20,30,100"
command = config.split()
vlans = command[-1].split(',')
print(vlans)