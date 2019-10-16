#!/usr/bin/env python3
#A program that calculates shipping charge

def shipping_charge(weight):
    if weight < 0:
        print("Can't calculate shipping charge of negative weights")
    elif weight > 10:
        print(weight*5.55)
        rate = 5.55
    elif weight > 5:
        rate = 4.05
    elif weight >2:
        rate = 2.35
    else:
        rate =1.25
    return weight * rate

weight = float(input("Please enter the weight of items: "))
print('Your shipping charge is :${:,.2f}'.format(shipping_charge(weight)))
