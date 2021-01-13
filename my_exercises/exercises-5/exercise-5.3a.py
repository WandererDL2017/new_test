questions = {
     "access_mode" : [
     "Введите номер VLAN: "          
     ],
     "trunk_mode" : [  
     "Введите разрешенные VLANы: "
     ]
}

mode_templates = {
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
mode = input("Введите режим работы интерфейса (access/trunk): " )

question = '{}_mode'.format(mode)

interface = input("Введите тип и номер интерфейса: ")
vlans = input('\n'.join(questions[question]).format())

name_mode = '{}_template'.format(mode)

print('interface {}'.format(interface))
print('\n'.join(mode_templates[name_mode]).format(vlans))