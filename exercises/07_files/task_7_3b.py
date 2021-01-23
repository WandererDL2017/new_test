# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan_input = input('введите номер vlan: ')

with open('exercises/07_files/CAM_table.txt') as macs:
    for line in macs:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, type, ports = words
            if vlan_input == vlan:
                print(f'{vlan:9}{mac:20}{ports}')