#!/usr/bin/env python3

import re                  # regex, a way to recognize expressions 

import sys                 # sys is how we get the file into our program 

file_name = sys.argv[1]    # the argument/file that is passed in will be known as file_name

acceptableMenuOptions = ['1','2','3','4','5','6'] #lines 9-50 are a series of functions that handle how the main menu works     
 
wdyn = 'What do you need? \n'

menuOptions = '''
\t\t\tMain Menu
1 = View a list of uniq IPs by IP address
2 = View a list of IPs from least to most frequent 
3 = View a list of IPs from most to least frequent
4 = View which Protocols appear in the log file  
5 = View the number of lines in the file
6 = Exit
'''

def menu_check(selection):
   if selection in acceptableMenuOptions:
       return selection
   print(selection+' is not a valid menu option')    
   print('\n\t---Please enter a valid menu option--- \n')
   return 0
def print_menu():
   print(menuOptions)
def main_menu():
   again = True
   while again:
       print_menu()
       need = menu_check((input(wdyn)))
       while need  == '0':
           need = menu_check((input(wdyn)))
       if need == '1':
           uniq_ips()
       if need == '2':
           sorted_uniq_ips()
       if need == '3':
           decending_sorted_uniq_ips()
       if need == '4':
           cat_protocols()
       if need == '5':
           line_counter()
       if need == '6':
           print('\n\t\t Thanks for using Vipre!\n')
           again = False

#below up to 160 are all the funcitons that are called from the menu            

def uniq_ips():                                  #uniq_ips() prepares a list of all the ip addresses in the file
  with open(file_name) as fh:
   fstring = fh.readlines()
   
  pattern = re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
# initializing the list object
  iplst=[]
 
# extracting the IP addresses
  for line in fstring:
    iplst.append(pattern.search(line)[0].strip())
  ip_counter(iplst)

def ip_counter(iplst):                        #ip_counter() counts the list of ip addresses and prints them 
  uniq_ip_adds = {}
  for x in iplst:
    if x not in uniq_ip_adds:
      uniq_ip_adds[x] = 1
    elif x in uniq_ip_adds:
      uniq_ip_adds[x] += 1
  sorted_ips = sorted(uniq_ip_adds.items())
  print('\t     IP Address                 # of times')
  print('\t   _______________              ____________\n')
  for ip, amount in sorted_ips:
    print("\t{:^20} -------- {:>8}".format(ip, amount))

def sorted_uniq_ips():                               #sorted_ips() sorts the list of all the ip addresses in the file
  with open(file_name) as fh:
   fstring = fh.readlines()
  pattern = re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
# initializing the list object
  iplst=[]
 
# extracting the IP addresses
  for line in fstring:
    iplst.append(pattern.search(line)[0].strip())
  sorted_ip_counter(iplst)

#this funtion counts and prints the sorted ip adresses 
def sorted_ip_counter(iplst):
  uniq_ip_adds = {}
  for x in iplst:
    if x not in uniq_ip_adds:
      uniq_ip_adds[x] = 1
    elif x in uniq_ip_adds:
      uniq_ip_adds[x] += 1
  sorted_ips = sorted(uniq_ip_adds.items(), key=lambda x:x[1])
  print('\t     IP Address                 # of times')
  print('\t   _______________              ____________\n')
  for ip, amount in sorted_ips:
    print("\t{:^20} -------- {:>8}".format(ip, amount))

#This funtion sorts the ip addresses and puts them in a list     
def decending_sorted_uniq_ips():
  with open(file_name) as fh:
   fstring = fh.readlines()
  pattern = re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
# initializing the list object
  iplst=[]
 
# extracting the IP addresses
  for line in fstring:
    iplst.append(pattern.search(line)[0].strip())
  rev_ip_counter(iplst)

# this function takes the list of sorted ip addresses and prints them in reverse order 
def rev_ip_counter(iplst):
  uniq_ip_adds = {}
  for x in iplst:
    if x not in uniq_ip_adds:
      uniq_ip_adds[x] = 1
    elif x in uniq_ip_adds:
      uniq_ip_adds[x] += 1
  sorted_ips = sorted(uniq_ip_adds.items(), key=lambda x:x[1], reverse = True)
  print('\t     IP Address                 # of times')
  print('\t   _______________              ____________\n')
  for ip, amount in sorted_ips:
    print("\t{:^20} -------- {:>11}".format(ip, amount))

# this function opens the file so each line can be read one at a time 
def cat_protocols():
  with open(file_name) as fh:
   fstring = fh.readlines()
  protocol_search(fstring)

# this function searches the open file for the words in the protocol_names list 
def protocol_search(fstring):
  protocol_names = ['HTTP', 'TCP', 'UDP', 'FTP', 'ICMP', 'HTTPS',
'SSH' , 'TELNET', 'DNS']
  dict_of_protos = {}
  for line in fstring:
    for protocol in protocol_names:
      if protocol in line:
        if protocol not in dict_of_protos:
          dict_of_protos[protocol] = 1
        else:
          dict_of_protos[protocol] += 1
  print('\t\t Protocol          # of times')
  print('\t\t __________         ___________\n')
  for ip, amount in dict_of_protos.items():
    print('\t{:^23} {:>11}'.format(ip, amount))

# this function counts the lines in a file
def line_counter():
  with open(file_name) as fh:
   fstring = fh.readlines()
  print('number of lines = '+str(len(fstring)))

# This is the first funciton that is called, it welcomes the user takes them to the menu 
def welcome_screen():
  print(''' \n\t\t\t Welcome to Vipre!
  \nEnter a number for one of the menu options to see some information about the log
  
  *Please make sure there are no blank lines in the file
  *Please make sure it is a txt file
  
           ___________________
           | _______________ |
           | | 192.168.0.1 | |
           | | TCP         | |
           | | 127.0.0.1   | |
           | | SSH         | |                ___
           | | 8.8.8.8 DNS | |             >-< _* \       ______        
           |_________________|                   \ \     /  ___  \     //
               _[_______]_                        \ \___/ /    \  \___//
           ___[___________]___                     \_____/      \_____/
          |         [_____] []|
          |         [_____] []|  
          L___________________J    
           ___________________      
          /###################\    
  \n \t\t\t Made by AEA
  ''')
  input('Hit enter to continue\n\n')
  main_menu()

welcome_screen()