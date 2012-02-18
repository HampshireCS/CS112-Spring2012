#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = inputnums()

print "Before sort:"
print nums

N=len(nums)-1
for x in range(N)
    p=x
    for i in range(x+1 N):
        if nums[i]<nums[p]:
            pos=i
   nums[x],nums[p]=nums[p],nums[x]

print "After sort:"
print nums
