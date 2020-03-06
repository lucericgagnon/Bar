# Read file in a directory

import os
import re
from ciscoconfparse import CiscoConfParse
from ciscoconfparse.ccp_util import IPv4Obj

def parse_intTRUNK():
   # parse = CiscoConfParse(file)
    trunks = parse.find_parents_w_child("^interface","switchport trunk")
    print('** Interface Trunk **')
    for intf in trunks:
        print (intf)

def parse_intNoSwitch():
   # parse = CiscoConfParse(file)
    noswitch = parse.find_parents_w_child("^interface","no switchport")
    print('** Interface Route **')
    for intf in noswitch:
        print (intf)        

def parse_IPv4():
   # parse = CiscoConfParse(file)
    #INTF_RE = re.compile(r'interface\s\S+')
    #ADDR_RE = parse.find_objects(r'address\s(\S+\s+\S+)')
    #ADDR_RE = parse.find_objects(r'ip\saddress')
    for obj in parse.find_objects(r'ip\saddress\s(\S+\s+\S+)'):
        #print ("Objet:", obj, "config:",obj.text)
        #nxip  = re.search('\s+ip\saddress\s(\d+.\d+.\d+.\d+)(/\d+)', obj.text)
        nxip  = re.search('\s+ip\saddress\s(\d+.\d+.\d+.\d+)\s(\d+.\d+.\d+.\d+)', obj.text)
        print ("IP add:",nxip.group(1), "Netmask",nxip.group(2))

dir ="C:/Users/Utilisateur/Documents/Visual Studio 2015/Projects/MyFirstProject/Parse_config_V1/Parse_config_V1/configs"
for files in os.listdir(str(dir)):
                filename = dir + "/" + files
                if os.path.isfile(filename):
                    parse = CiscoConfParse(filename)
                    print (filename)
                    parse_intTRUNK()
                    parse_intNoSwitch()
                    parse_IPv4()

                else:
                    print ("invalid file : ",filename)



