#!/usr/bin/env python3
my_list =["192.168.0.1",5060,"UP"]
print("The first item is the list (IP): "+ my_list[0])
print("The second item is the list (IP): " + str(my_list[1]))
print("The third item is the list (IP): " + my_list[2])
new_list = [5060, "80", 55, "10.0.0.1","10.20.30.1","ssh"]
print(f"When I {new_list[-1]} into IP address {new_list[-2]} or {new_list[-3]}. I am unable to ping ports str({new_list[0]}), str({new_list[1]}), or str({new_list[2]}).")
