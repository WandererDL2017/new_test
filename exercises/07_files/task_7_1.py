# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ospf_route = open("exercises/07_files/ospf.txt")
ospf_route = ospf_route.readlines()



for ospf in ospf_route:
    ospf = ospf.split()
    ospf.remove('O')
    ospf.remove('via')
    prefix, adMetric, nextHop, lastUpdate, outboundInterface = ospf

    adMetric = adMetric.strip('[]')
    nextHop = nextHop.strip(',')
    lastUpdate = lastUpdate.strip(',')

    template_ospf = """
                Prefix                  {}             
                AD/Metric               {}  
                Next-Hop                {}  
                Last update             {}  
                Outbound Interface      {}
                """

    print(template_ospf.format(prefix, adMetric, nextHop, lastUpdate, outboundInterface))