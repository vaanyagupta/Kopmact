import bz2
import binascii
import os

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
