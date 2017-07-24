import tarfile

flag=True
y=[]
while(flag):
    print("1.Archieve a file")
    print("2.(de)Archieve a file")
    print("3.exit")
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
    else:
        break
    
        
