# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

config_sw1_cleared = open('exercises/07_files/config_sw1_cleared.txt', 'w')

with open('exercises/07_files/config_sw1.txt') as config:
    for line in config:
        for word in ignore:
            if word in line:
                config_sw1_cleared.write(line)