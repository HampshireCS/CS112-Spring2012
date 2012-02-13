#!/usr/bin/env python
var1=0
var2=[]
var3=None
while var3!="":
    var3=raw_input()
    var2.append(float(var3))
for var in var2:
    var1+=var
print var1/len(var2)
