import os
import matplotlib.pyplot as plt
import csv
import tarfile
import gzip
import shutil
import bz2
import binascii
import lzma
import csv
import matplotlib.pyplot as plt
import plotly.plotly as py

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
            #tar = input("Enter the filename as 'fortar.py' for archieving: ")
            #os.system('python ' +str(tar))
            for_tar()
            
        elif(int(x)==2):
            #bz = input("Enter the filename as 'forbz2.py' for bz2 compression: ")
            #os.system('python ' +str(bz))
            for_bz()
        elif(int(x)==3):
            #gzip = input("Enter the filename as 'forgzip.py' for gzip compression: ")
            #os.system('python ' +str(gzip))
            for_gzip()
        elif(int(x)==4):
            #lzma = input("Enter the filename as 'forlzma.py' for lzma compression: ")
            #os.system('python ' +str(lzma))
            for_lzma()

def for_tar():
    print("tar Archieving")
    flag=True
    y=[]
    while(flag):
        print("1.Archieve a file")
        print("2.(de)Archieve a file")
        print("3.Upload file to drive")
        print("4.exit")
        ch=input("Enter your choice.")
        if(int(ch) == 1):
            #Archive
            while(True):
                z=input("Want to add more file(y/n) : ")
                if(z=='y'):
                    x=input("Enter file name : ")
                    y.append(x)
                else:
                    break

            print ('creating archive')
            print (y)

            out = tarfile.open('tarfile_add.tar', mode='w')
            for c in y:
                out.add(str(c))

            t = tarfile.open('tarfile_add.tar', mode='r')
            for member_info in t.getmembers():
                print (member_info.name)

        elif(int(ch)==2):
            tar = tarfile.open("tarfile_add.tar")
            tar.extractall()
            tar.close()
        elif(int(ch)==3):
            r=input("Enter file name to upload")
            os.system('python ' +'driveupload.py '+r)
        else:
            break


def for_gzip():
    print("compression and deccompression using gzip")
    flag=True
    while(flag):
        print("1.compress a file")
        print("2.(de)compress a file")
        print("3.Upload file to drive")
        print("4.exit")
        ch=input("Enter your choice.")
        if(int(ch) == 1):
            #compress
            x=input("Enter file name : ")
            z=str(x).split('.')
            inF = open(x, 'rb')
            s = inF.read()
            inF.close()

            outF=gzip.GzipFile("compressedByGZIP.gz",'wb')
            outF.write(s)
            outF.close()
        elif(int(ch) == 2):
            #decompress
            inF = gzip.GzipFile("compressedByGZIP.gz", 'rb')
            s = inF.read()
            inF.close()

            outF = open("x1."+str(z[1]), 'wb')
            outF.write(s)
            outF.close()
        elif(int(ch)==3):
            r=input("Enter file name to upload")
            os.system('python ' +'driveupload.py '+r)
        else:
            break

        
    c=os.path.getsize(x)
    d=os.path.getsize("compressedByGZIP.gz")


    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
     
    objects = ("original","compressed")
    y_pos = np.arange(len(objects))
    performance = [c,d]
    plt.barh(y_pos, performance, align='center')
    plt.yticks(y_pos, objects)
    plt.xlabel('ratio')
    plt.title('Compression')
     
    plt.show()



def for_bz2():
    print("compression and deccompression using bzip2")
    flag=True
    while(flag):
        print("1.compress a file")
        print("2.(de)compress a file")
        print("3.Upload file to drive")
        print("4.exit")
        ch=input("Enter your choice.")
        if(int(ch) == 1):
            #compress
            x=input("Enter file name : ")
            z=str(x).split('.')
            inF = open(x, 'rb')
            s = inF.read()
            inF.close()

            outF=bz2.BZ2File("compressedByBZ2.bz",'wb')
            outF.write(s)
            outF.close()
        elif(int(ch) == 2):
            #decompress
            inF = bz2.BZ2File("compressedByBZ2.bz", 'rb')
            s = inF.read()
            inF.close()

            outF = open("x1."+str(z[1]), 'wb')
            outF.write(s)
            outF.close()

        elif(int(ch)==3):
            r=input("Enter file name to upload")
            os.system('python ' +'driveupload.py '+r)

        else:
            break

    c=os.path.getsize(x)
    d=os.path.getsize("compressedByBZ2.bz")


    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
     
    objects = ("original","compressed")
    y_pos = np.arange(len(objects))
    performance = [c,d]
    plt.barh(y_pos, performance, align='center')
    plt.yticks(y_pos, objects)
    plt.xlabel('ratio')
    plt.title('Compression')
     
    plt.show()


def for_lzma():
    print("compression and decompression using LZma 2")
    flag=True
    while(flag):
        print("1.compress a file")
        print("2.(de)compress a file")
        print("3.Upload file to drive")
        print("4.exit")
        ch=input("Enter your choice.")
        if(int(ch) == 1):
            #compress
            x=input("Enter file name : ")
            inF = open(x, 'rb')
            z=str(x).split('.')
            s = inF.read()
            inF.close()

            outF=lzma.LZMAFile("compressedByXZ.xz",'wb')
            outF.write(s)
            outF.close()

        elif(int(ch) == 2):
            #decompress
            inF = lzma.LZMAFile("compressedByXZ.xz", 'rb')
            s = inF.read()
            inF.close()

            outF = open("x1."+str(z[1]), 'wb')
            outF.write(s)
            outF.close()
        elif(int(ch)==3):
            r=input("Enter file name to upload")
            os.system('python ' +'driveupload.py '+r)
        else:
            break

    c=os.path.getsize(x)
    d=os.path.getsize("compressedByXZ.xz")


    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
     
    objects = ("original","compressed")
    y_pos = np.arange(len(objects))
    performance = [c,d]
    plt.barh(y_pos, performance, align='center')
    plt.yticks(y_pos, objects)
    plt.xlabel('ratio')
    plt.title('Compression')
     
    plt.show()



    
if(os.path.getsize("output.csv") == 0):
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
                #os.system('python ' +tar)
                for_tar()
            else:
                manualcall()
            
        elif(v2>=v1 and v2>=v3 and v2>=v4):
            print("the prefered one is bz2 compression ")
            rt=input("Do you want to continue (y/n) : ")
            if(rt=='y'):
                bz = 'forbz2.py'
                #os.system('python ' +bz)
                for_bz()
            else:
                manualcall()
            
        elif(v3>=v2 and v3>=v1 and v3>=v4):
            print("the prefered one is gzip compression ")
            rt=input("Do you want to continue (y/n) : ")
            if(rt=='y'):
                gzip = 'forgzip.py'
                #os.system('python ' +gzip)
                for_gzip()
            else:
                manualcall()

            
        elif(v4>=v2 and v4>=v3 and v4>=v1):
            print("the prefered one is lzma compression ")
            rt=input("Do you want to continue (y/n) : ")
            if(rt=='y'):
                lzma = 'forlzma.py'
                #os.system('python ' +lzma)
                for_lzma()
            else:
                manualcall()

            
    elif(int(ch2)==2):
        lzma = 'forlzma.py'
        #os.system('python ' +lzma)
        for_lzma()

    elif(int(ch2)==3):
        manualcall()
    elif(int(ch2)==4):
        userstat()

