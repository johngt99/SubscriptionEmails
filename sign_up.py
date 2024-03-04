import csv
import os
clear = lambda: os.system('cls')
clear()
print("\nCreate an Account")


file = open('testcsv.csv','a+', newline='')
Writer = csv.writer(file)
list = [] 

val1 = '0'#0 to Normal Users / 1 to admin
val3 = 'no'
val4 = 'no'
val5 = 'no'
val6 = 'weekly'

email = input("\nEmail: ")
list.append([val1,email,val3,val4,val5,val6])
Writer.writerows(list)

#if email and pass valid login
clear()
file.seek(0)
file.close()

print("Account Created")
print("Login?")#send to signup
print("\n 1. Yes\n 2. No. Leave")

res = input("\n Your Answer: ")

if res == '1':
    file.close()
    from main import *
else:
    file.close()
    quit()
