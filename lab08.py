#!/usr/bin/env python3
#Use dictionary to return the book or movie by promting user input
book_dic = {'1':'Harry Potter','2':'Hobbit & Lord of the Rings','3':'Chronicles of Narnia','4':'Indiana Jones'}

def book_name(number):
    if int(number) < 1 or int(number) >5:
        print("The book you are looking for does not exsit.")
    else:
        return book_dic.get(user_input)
user_input = input("Please enter the book series number: ")
print("The book you are looking for is: ",book_name(user_input))

