#!/usr/bin/env python3
#open file
dnsfile = open("dnsservers.txt")
#create list of lines
dnslist = dnsfile.readlines()
#loop over lines
for eachitem in dnslist:
    print(eachitem, end="")
#close file
dnsfile.close()
