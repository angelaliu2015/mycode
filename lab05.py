#!/usr/bin/env python3
dic = {"Flash":{"Speed": "Fastest", "Intelligence": "Lowest", "Strength": "Lowest"}, "Batman":{"Speed": "Slowest", "Intelligence": "Highest", "Strength": "Money"}, "Superman":{"Speed": "Fast", "Intelligence": "Average", "Strength": "Strongest"}}
char_name = input("which character do you want to know about?(Flash, Batman, Superman) :")
char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence) :")
subdic = dic.get(char_name)
#print("The character you want to know: ")
#print(dic.get(char_name," the name does not present"))
#print(subdic.get(char_stat,"the statistic do you want to know about does not present"))
print(char_name,"'s",char_stat,' is: ',subdic.get(char_stat))
print(f"{char_name}'s {char_stat} is: {dic.get(char_name).get(char_stat)}")
