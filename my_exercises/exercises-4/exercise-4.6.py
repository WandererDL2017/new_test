ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route = ospf_route.split()
ospf_route.remove('via')

prefix, adMetric, nextHop, lastUpdate, outboundInterface = ospf_route

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