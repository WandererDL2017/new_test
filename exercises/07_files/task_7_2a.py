# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
with open('exercises/07_files/config_sw1.txt') as config:
  for line in config:
    for word in ignore:
      if line.startswith('!') or word in line:
        break
    else:
      print(line.rstrip())