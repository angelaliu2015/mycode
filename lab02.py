#!/usr/bin/env python3
col_list = ["blue","Columbus"]
col_list.append(1492)
user_input =input("What is the name?: ")
col_list.append(user_input)
print(f"In {col_list[-2]}, {col_list[1]} sailed the ocean {col_list[0]}. {col_list[-1]} fell off the boat.")

