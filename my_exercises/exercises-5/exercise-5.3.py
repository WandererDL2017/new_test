mode = input("Введите режим работы интерфейса (access/trunk): " )
interface = input("Введите тип и номер интерфейса: ")
vlans = input("Введите номер влан(ов): ")

mode_template = {
        'access_template' : [
        "switchport mode access", "switchport access vlan {}",
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable"
        ],
        'trunk_template' : [
        "switchport trunk encapsulation dot1q", "switchport mode trunk",
        "switchport trunk allowed vlan {}"
        ]
}

name_mode = '{}_template'.format(mode)

print('interface {}'.format(interface))
print('\n'.join(mode_template[name_mode]).format(vlans))