import csv
file=open('testcsv.csv','r')
file.seek(0)
Reader=csv.reader(file)
for row in Reader:
    to = row[1]
    if row[2] == 'yes' and (row[3] == 'yes' and row[4] == 'yes'):
        from cars import *
        from games import *
        from music import *
        #print(row[1], '123')
    elif row[2] == 'yes' and (row[3] == 'yes' and row[4] == 'no'):
        from cars import *
        from games import *
        #print(row[1], '12')
    elif row[2] == 'yes' and (row[4] == 'yes' and row[3] == 'no'):
        from cars import *
        from music import *
        #print(row[1], '13')
    elif row[3] == 'yes' and (row[4] == 'yes' and row[2] == 'no'):
        from games import *
        from music import *
        #print(row[1], '23')
    elif row[2] == 'yes' and (row[3] == 'no' and row[4] == 'no'):
        from cars import *
        #print(row[1], '1')
    elif row[3] == 'yes'  and (row[2] == 'no' and row[4] == 'no'):
        from games import *
        print(row[1], '2')
    elif row[4] == 'yes'  and (row[2] == 'no' and row[3] == 'no'):
        from music import *
        #print(row[1], '3')  






