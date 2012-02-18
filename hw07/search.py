#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums=inputNums()
sorted(nums)
print "I have sorted your numbers"
x=raw_input("Which number should I find: ")
m=1
M=len(nums)-1
while M>=m:
    md=M+m/2
    if nums[md]==x:
        break
    elif x>nums[md]:
       m=md+1
     else:
        M-=1
if nums[md]=x:
    print "Found", x "at", md
else
    print "Could not find", x
