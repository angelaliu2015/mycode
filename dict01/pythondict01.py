#!/usr/bin/env pythons
##create a dictionary
switch = {'hostname': 'sw1','ip':'10.0.1.1', 'version':'1.2', 'vendor':'cisco'}

##display parts of the dictionary

print(switch['hostname'])
print(switch['ip'])
input("press enter to error out.")
#print(switch['lynx'])

print("First test - .get()")
print(switch.get('lynx'))
print("Second test -.get()")
print(switch.get('lynx', "the key is in another castle!"))
print("Third test - .get()")
print(switch.get('version'))

print("Fourth test - .keys()")
print(switch.keys())

print("Fifth test - .values()")
print(switch.values())

print("Sixth test - .pop()")
switch.pop('version')
print(switch.keys())
print(switch.values())

print("Seventh test - Add a new value")
switch['adminlogin'] = 'kar108'
print(switch.keys())
print(switch.values())

print("Enghth test - Add a new value")
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())

