import os
import matplotlib.pyplot as plt
import csv

def printstat():
    print("Enter the type of compression you want do: ")
    print("1.Enter the filename as 'fortar.py' for archieving: ")
    print("2.Enter the filename as 'forbz2.py' for bz2 compression: ")
    print("3.Enter the filename as 'forgzip.py' for gzip compression: ")
    print("4.Enter the filename as 'forlzma.py' for lzma compression: ")
    print("5.Want to see user selection stats (y/n)? ")

def userstat():
    y=[]
    with open('output.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                y.append(int(', '.join(row)))
    plt.plot(y)
    plt.ylabel('User choice')
    plt.xlabel('Every new entry')
    plt.show()


    
def manualcall():
    y=[]
    printstat()
    x=input("Choose your option : ")
    if(x=='y' or x=='n'):
        if(x=='y'):
            userstat()
        else:
            manualcall()
    else:
        y.append(x)
        resultFyle = open("output.csv",'a+')
        for r in y:
            resultFyle.write(r + "\n")
        resultFyle.close()
        if(int(x)==1):
            tar = input("Enter the filename as 'fortar.py' for archieving: ")
            os.system('python ' +str(tar))
            
        elif(int(x)==2):
            bz = input("Enter the filename as 'forbz2.py' for bz2 compression: ")
            os.system('python ' +str(bz))

        elif(int(x)==3):
            gzip = input("Enter the filename as 'forgzip.py' for gzip compression: ")
            os.system('python ' +str(gzip))

        elif(int(x)==4):
            lzma = input("Enter the filename as 'forlzma.py' for lzma compression: ")
            os.system('python ' +str(lzma))
            
    
if(os.path.getsize("foo.csv") == 0):
    manualcall()

else:
    resultFyle = open("output.csv",'r+')
    v1=0
    v2=0
    v3=0
    v4=0
    print("""
1.Preffered one
2.Suggested one(lzma2 Compression)
3.Manual
4.user stats
    """)
    ch2 = input("choice : ")
    
    with open('output.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if(int(', '.join(row))==1):
                v1=v1+1
            elif(int(', '.join(row))==2):
                v2=v2+1
            elif(int(', '.join(row))==3):
                v3=v3+1
            elif(int(', '.join(row))==4):
                v4=v4+1
    if(int(ch2)==1):
        if(v1>=v2 and v1>=v3 and v1>=v4):
            print("the prefered one is tar archieving ")
            rt=input("Do you want to continue (y/n) : ")
            if(rt=='y'):
                tar = 'fortar.py'
                os.system('python ' +tar)
            else:
                manualcall()
            
        elif(v2>=v1 and v2>=v3 and v2>=v4):
            print("the prefered one is bz2 compression ")
            rt=input("Do you want to continue (y/n) : ")
            if(rt=='y'):
                bz = 'forbz2.py'
                os.system('python ' +bz)
            else:
                manualcall()
            
        elif(v3>=v2 and v3>=v1 and v3>=v4):
            print("the prefered one is gzip compression ")
            rt=input("Do you want to continue (y/n) : ")
            if(rt=='y'):
                gzip = 'forgzip.py'
                os.system('python ' +gzip)
            else:
                manualcall()

            
        elif(v4>=v2 and v4>=v3 and v4>=v1):
            print("the prefered one is lzma compression ")
            rt=input("Do you want to continue (y/n) : ")
            if(rt=='y'):
                lzma = 'forlzma.py'
                os.system('python ' +lzma)
            else:
                manualcall()

            
    elif(int(ch2)==2):
        lzma = 'forlzma.py'
        os.system('python ' +lzma)

    elif(int(ch2)==3):
        manualcall()
    elif(int(ch2)==4):
        userstat()

