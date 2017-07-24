import csv
v1=0
v2=0
v3=0
v4=0
with open('output.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
        if(int(', '.join(row))==1):
            v1=v1+1
        elif(int(', '.join(row))==2):
            v2=v2+1
        elif(int(', '.join(row))==3):
            v3=v3+1
        elif(int(', '.join(row))==4):
            v4=v4+1
print(max(v1,v2,v3,v4))
v1=2
if(v1>=v2 and v1>=v3 and v1>=v4):
    print("v1")
elif(v2>=v1 and v2>=v3 and v2>=v4):
    print("v2")
elif(v3>=v2 and v3>=v1 and v3>=v4):
    print("v3")
elif(v4>=v2 and v4>=v3 and v4>=v1):
    print("v4")


            
print("""   hi
hello""")
