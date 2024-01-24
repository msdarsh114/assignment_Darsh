#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     18-12-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import array as arr

n=int(input("Enter the size of array : "))

a=arr.array('i',[])

for i in range(n):
    x=int(input("enter the array elements: "))
    a.append(x)

print(a)