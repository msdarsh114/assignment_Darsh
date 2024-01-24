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
import keyword as k

keys=["darsh","ach","else","anu","if","elif"]

for i in range(len(keys)):
    if k.iskeyword(keys[i]):
        print(keys[i] + " is python keyword")
    else:
        print(keys[i] + " is not python keyword")