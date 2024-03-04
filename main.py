import os
clear = lambda: os.system('cls')
clear()

from verification import *
clear()

bigloop = 1
while bigloop == 1:
    #print("\n")
    print(" MENU       ", email,"\n")

    import csv
    file=open('testcsv.csv','r')
    Reader=csv.reader(file)
    list=[]
    found=False
    
    for row in Reader:
        if row[1] == email:
            found=True
            print('\n Subscribed to Cars: ', row[2])
            print(' Subscribed to Games: ', row[3])
            print(' Subscribed to Music: ', row[4])
        list.append(row)
    file.close()

    print("\n 1. Manage Subscriptions")
    print(" 2. Exit\n")

    res= int(input('\n Your Answer: '))

    loop = 1

    if res == 1:
        while loop == 1:
            clear()
            file=open('testcsv.csv','r')
            Reader=csv.reader(file)
            list=[]
            found=False
            for row in Reader:
                if row[1] == email:
                    found=True
                    print('\n Subscribed to Cars: ', row[2])
                    print(' Subscribed to Games: ', row[3])
                    print(' Subscribed to Music: ', row[4])
                    print(' Frequency: ', row[5])
                list.append(row)
            file.close()

            print("\n 1. Change Cars Subscription")
            print(" 2. Change Games Subscription")
            print(" 3. Change Music Subscription")
            print(" 4. Change Frequency")
            print(" 5. Back\n")

            ans = int(input('\n Your Answer: '))

            if ans == 1:
                file=open('testcsv.csv','r')
                Reader=csv.reader(file)
                list=[]
                found=False
                for row in Reader:
                    if row[1] == email:
                        found=True
                        if row[2] == 'no':
                            row[2] = 'yes'
                        elif row[2] == 'yes':
                            row[2] = 'no'
                        else:
                            row[2] = 'no'
                    list.append(row)
                file.close()
                        
                file=open('testcsv.csv', 'w+',newline='')
                Writer=csv.writer(file)
                Writer.writerows(list)
                file.seek(0)        
                file.close()
            elif ans == 2:
                file=open('testcsv.csv','r')
                Reader=csv.reader(file)
                list=[]
                found=False
                for row in Reader:
                    if row[1] == email:
                        found=True
                        if row[3] == 'no':
                            row[3] = 'yes'
                        elif row[3] == 'yes':
                            row[3] = 'no'
                        else:
                            row[3] = 'no'
                    list.append(row)
                file.close()
                        
                file=open('testcsv.csv', 'w+',newline='')
                Writer=csv.writer(file)
                Writer.writerows(list)
                file.seek(0)        
                file.close()
            elif ans == 3:
                file=open('testcsv.csv','r')
                Reader=csv.reader(file)
                list=[]
                found=False
                for row in Reader:
                    if row[1] == email:
                        found=True
                        if row[4] == 'no':
                            row[4] = 'yes'
                        elif row[4] == 'yes':
                            row[4] = 'no'
                        else:
                            row[4] = 'no'
                    list.append(row)
                file.close()
                        
                file=open('testcsv.csv', 'w+',newline='')
                Writer=csv.writer(file)
                Writer.writerows(list)
                file.seek(0)
                file.close()
            elif ans == 4:
                file=open('testcsv.csv','r')
                Reader=csv.reader(file)
                list=[]
                found=False
                for row in Reader:
                    if row[1] == email:
                        found=True
                        if row[5] == 'weekly':
                            row[5] = 'monthly'
                        elif row[5] == 'monthly':
                            row[5] = 'weekly'
                        else:
                            row[4] = 'weekly'
                    list.append(row)
                file.close()
                        
                file=open('testcsv.csv', 'w+',newline='')
                Writer=csv.writer(file)
                Writer.writerows(list)
                file.seek(0)
                file.close()
            elif ans == 5:
                loop = 0
                clear()
                #from menu import *
            else:
                clear()
                print('\n No change was made. \n')
                loop = 1
    else:
        bigloop = 0
        quit()



# if lista[1] == yes:
#     print("\nMandar email sobre Opcao 1")
# if lista[2] == yes:
#     print("\nMandar email sobre Opcao 2")
# if lista[2] == yes:
#     print("\nMandar email sobre Opcao 3")
