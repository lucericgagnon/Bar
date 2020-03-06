# Read file in a directory

import os
import re
from ciscoconfparse import CiscoConfParse
from ciscoconfparse.ccp_util import IPv4Obj

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def parse_intTRUNK():
   # parse = CiscoConfParse(file)
    trunks = parse.find_parents_w_child("^interface","switchport trunk")
    #print('** Interface Trunk **')
    for intf in trunks:
        print (intf)

def parse_intNoSwitch():
   # parse = CiscoConfParse(file)
    noswitch = parse.find_parents_w_child("^interface","no switchport")
    #print('** Interface Route **')
    #for intf in noswitch:
     #   print (intf)        

def parse_IPv4():

    for obj in parse.find_objects(r'ip\saddress\s(\S+\s+\S+)'):
        nxip  = re.search('\s+ip\saddress\s(\d+.\d+.\d+.\d+)\s(\d+.\d+.\d+.\d+)', obj.text)
        #print ("IP add:",nxip.group(1), "Netmask",nxip.group(2))

l3_interface_type = {}
l2_interface_type = {}
dir ="C:/Users/Utilisateur/Documents/Visual Studio 2015/Projects/MyFirstProject/Parse_config_V1/Parse_config_V1/mtmdet/configs"
for files in os.listdir(str(dir)):
                filename = dir + "/" + files
                if os.path.isfile(filename):
                    parse = CiscoConfParse(filename)
                    #print ("Du fichier ",filename)
                    #giga_interface = {}
                    #loop_interface = {}
                    
  
                    all_intfs = parse.find_objects(r"^interf")
                    ip_intfs = list()
                    acc_intfs = list()
                    for obj in all_intfs:
                        if obj.re_search_children(r"\s+ip\saddress\s(\d+.\d+.\d+.\d+)\s(\d+.\d+.\d+.\d+)"):
                            ip_intfs.append(obj)
                        if obj.re_search_children(r"\s+mode\saccess"):
                            acc_intfs.append(obj)    

                    #print(ip_intfs)
                    i = 0

                    print("*** Inteface avec adresses IP **")
                    for ojb in ip_intfs:
                        # print(ojb.group(1),'group 2', ojb.group(2))
                        i += 1
                        j = 0
                        #print('i = ',i,ojb)
                        #print(ojb.all_children)
                     
                        print("Interface: ",ojb.text)
                        #int_face = re.search(r'\s+G.+d+\/d+\/d+',obj.text)
                        #int_face = re.search(r'(\w+\d+(\/\d{1,2}|\/\d{1,2}\/\d+|\/\d{1,2}\.\d+|\/\d{1,2}\:\d+)?|\w+-\w+\d{1,3})',obj.text)
                        #int_face = re.search(r'interface\s+(D+\d+((/\d+)+(\.\d+)?))',obj.text)
                        #int_face = re.search(r'\interface\s(S+)',obj.text)
                        #int_face = re.search(r'interface(\D+)',ojb.text)
                        int_face = re.search(r'interface((\D+)(\d+)((/\d+)+(\.\d+)?)?)',ojb.text)
                        if int_face:
                            if int_face.group(2).strip()=='GigabitEthernet':
                                #print('GigabitEthernet')
                                if 'GigabitEthernet' in l3_interface_type:
                                    l3_interface_type['GigabitEthernet'] += 1
                                else:
                                    l3_interface_type['GigabitEthernet'] = 1    
                                    
                            elif int_face.group(2).strip()=='Loopback':
                                #print('Loopback')
                                if 'Loopback' in l3_interface_type:
                                    l3_interface_type['Loopback'] += 1
                                else:
                                    l3_interface_type['Loopback'] = 1
                            elif int_face.group(2).strip()=='TenGigabitEthernet':
                                #print('TenGigabitEthernet')
                                if 'TenGigabitEthernet' in l3_interface_type:
                                    l3_interface_type['TenGigabitEthernet'] += 1
                                else:
                                    l3_interface_type['TenGigabitEthernet'] = 1
                            elif int_face.group(2).strip()=='Vlan':
                                #print('TenGigabitEthernet')
                                if 'TenGigabitEthernet' in l3_interface_type:
                                    l3_interface_type['Vlan'] += 1
                                else:
                                    l3_interface_type['Vlan'] = 1
                            elif int_face.group(2).strip()=='ve':
                                #print('TenGigabitEthernet')
                                if 've' in l3_interface_type:
                                    l3_interface_type['ve'] += 1
                                else:
                                    l3_interface_type['ve'] = 1
                            elif int_face.group(2).strip()=='ethernet':
                                #print('TenGigabitEthernet')
                                if 'ethernet' in l3_interface_type:
                                    l3_interface_type['ethernet'] += 1
                                else:
                                    l3_interface_type['ethernet'] = 1
                            elif int_face.group(2).strip()=='management':
                                #print('TenGigabitEthernet')
                                if 'management' in l3_interface_type:
                                    l3_interface_type['management'] += 1
                                else:
                                    l3_interface_type['management'] = 1         
                            else:    

                                #print ("Interface no: ",int_face.group(1))
                                #print ("intf gp 2 ",int_face.group(2))
                                print ("Interface no: ",obj.text)
                        """
                        
                        for obj in ojb.all_children:
                            j += 1
                            print('j = ',j,obj)
                            nxip  = re.search(r'\s+ip\saddress\s(\d+.\d+.\d+.\d+)\s(\d+.\d+.\d+.\d+)',obj.text)
                            if nxip:
                                print ("  IP add:",nxip.group(1), "Netmask:",nxip.group(2))
                            desc = re.search(r'\s+description\s(\S+)',obj.text)
                            if desc:
                                print ("  description>",desc.group(1))
                            vrfs = re.search(r'\s+vrf forwarding\s(\S+)',obj.text)
                            if vrfs:
                                print ("  VRF>",vrfs.group(1))
                            vlans = re.search(r'\s+switchport access vlan\s(\d+)',obj.text)
                            if vlans:
                                print ("  VLAN>",vlans.group(1))
                        """
                        print("<<<<<  Continue >>>>>>>>")
                        continue
                        print("*** Inteface en acces **")
                        for ojb in acc_intfs:
                         print(ojb.text)
                         for obj in ojb.all_children:
                            vlans = re.search(r'\s+switchport access vlan\s(\d+)',obj.text)
                            if vlans:
                                print ("  VLAN>",vlans.group(1))
                            desc = re.search(r'\s+description\s(\S+)',obj.text)
                            if desc:
                                print ("  description>",desc.group(1))

                else:
                    print ("invalid file : ",filename)
print(l3_interface_type)


# Met en ordre                     
liste_keys=(list(sorted(l3_interface_type.keys())))


# Debut construction table pour interface IP 
tbl_message = '\n\n'
tbl_message += '<table align = "left", border="1" ><tr bgcolor="#eee8aa" bordercolor="#408000">'
tbl_message += '<th>Type d'+"'"+'interface avec adrese IP</th>'
tbl_message += '<th>Nombre</th>'
tbl_message += '</tr>'

colorp="#4d88ff"
colori="#87CEFA"
i=2
for key in liste_keys:
    print(key,end=' ')
    print (l3_interface_type.get(key))
    #tbl_message += '<tr bgcolor="#4d88ff">'
    if i % 2 == 0:
        tbl_message += '<tr bgcolor='+ colorp + '>'
    else :
        tbl_message += '<tr bgcolor='+ colori + '>'
    i += 1
    print(' Valuer i = ',str(i))
    tbl_message += '<td>' + key + '</td>'
    tbl_message += '<td>' + str(l3_interface_type.get(key)) + '</td>'	
    tbl_message += '</tr>'
    
tbl_message += '<td valign="top">'
tbl_message += '</td>'

tbl_message += '</tr>'
tbl_message += '</td>'
tbl_message += '</table><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>'

message = MIMEText(tbl_message, 'html')
print ("\n\n TABLE \n\n")
print(message)

ftest = open("nb_interfaces.html", "wb")

ftest.write(bytes(message))


# Debut construction table pour interface niveau 2
tbl_message = '\n\n'
tbl_message += '<table align = "left", border="1" ><tr bgcolor="#eee8aa" bordercolor="#408000">'
tbl_message += '<th>Type d'+"'"+'interface de niveau 2</th>'
tbl_message += '<th>Nombre</th>'
tbl_message += '</tr>'

colorp="#4d88ff"
colori="#87CEFA"
i=2


message = MIMEText(tbl_message, 'html')
ftest.write(bytes(message))

ftest.close()



print('** FIN du programme **')


