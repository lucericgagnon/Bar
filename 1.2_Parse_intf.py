# Read file in a directory

import os
from ciscoconfparse import CiscoConfParse

def parse_intTRUNK(file):
    parse = CiscoConfParse(file)
    trunks = parse.find_parents_w_child("^interface","switchport trunk")
    for intf in trunks:
        print (intf)

dir ="C:/Users/Utilisateur/Documents/Visual Studio 2015/Projects/MyFirstProject/Parse_config_V1/Parse_config_V1/configs"
for files in os.listdir(str(dir)):
                filename = dir + "/" + files
                if os.path.isfile(filename):
                    
                    print (filename)
                    parse_intTRUNK(filename)
                    
                else:
                    print ("invalid file : ",filename)



