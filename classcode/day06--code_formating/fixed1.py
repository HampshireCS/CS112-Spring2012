#!/usr/bin/env python
"""
fixed1.py

Find the average of inputed numbers
"""

input_list = []
input_number = None

# get list of numbers from user
while input_number != "":
    input_number = raw_input("Enter a number: ")
    if input_number.isdigit():
        input_list.append(float(input_number)) 

# total the list of numbers
total = 0
for num in input_list:
    total += num

# print average of list
print total/len(input_list)
