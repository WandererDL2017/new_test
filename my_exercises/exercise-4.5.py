command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

list1 = command1.split()
list2 = command2.split()

vlans1 = list1[-1].split(',')
vlans2 = list2[-1].split(',')

vlans = set(vlans1) & set(vlans2)
vlans = list(vlans)
vlans.sort()

print(vlans)