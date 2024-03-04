import os
clear = lambda: os.system('cls')
clear()

import csv
file=open('testcsv.csv','r')
Reader=csv.reader(file)
list=[]


email = input("\n Enter user email: ") 
found=False
for row in Reader:
    if row[1] == email:
        found = True
        from main import * 
file.close()

if found==False:
    clear()
    print(" Your email doesn't exist.\n Create a new email?")#send to signup
    print("\n 1. Yes\n 2. No. Leave")

    res = input("\n Your Answer: ")

    if res == '1':
        file.close()
        from sign_up import *
    else:
        file.close()
        quit()
file.close()

