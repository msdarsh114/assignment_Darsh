#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     17-12-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def rec(x):
    if x==0:
        print(x)
    else:
        print(x)
        rec(x-1)


n=5
rec(n)