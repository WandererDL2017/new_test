nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat2 = nat.replace('Fast', 'Gigabit')
print(nat2)