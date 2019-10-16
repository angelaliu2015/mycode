#!/usr/bin/env python3
hostname = input("what valye should we set for hostname?")

if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname matches expected config.:")
else:
    print("Hostname does not exsit")

print("Exiting the script")
