import datetime
#if You need add more people just add name in clintlist 
clintlist=["Ravi","Rohan","Mohan","Sonu","Monu"]
clintindex=1
#Retrun Date and Time
def gettimedata():
    return str(datetime.datetime.now())
#Retrive data in file Function
def retrivedata(n):
    gettypework = input("Enter What You Want 1 : exc  &   2 : dite :- ")
    if(gettypework=="1"):
        indesx = clintlist[n]
        file_path = f"fitnes_data/{indesx}_exc.txt"
        fileopen = open(file_path,"a+")
        if (fileopen.read() == ""):
            print("No Data Found")
            fileopen.read()
        else:
            print(fileopen.read())
        fileopen.close()
    else:
        indesx = clintlist[n]
        file_path = f"fitnes_data/{indesx}_dite.txt"
        fileopen = open(file_path,"a+")
        if(fileopen.read()==""):
            print("No Data Found")
            fileopen.read()
        else:
            print(fileopen.read())
        fileopen.close()
#Insert Data Function
def insertdata(n):
    gettypework = input("Enter What You Want 1 : exc  &  2 : dite :- ")
    if(gettypework=="1"):
        indesx = clintlist[n]
        file_path = f"fitnes_data/{indesx}_exc.txt"
        fileopen = open(file_path,"a")
        insertdataline = input("Enter Your Data : ")
        fileopen.write(f"[ {gettimedata()} ] "+insertdataline + "\n")
        fileopen.close()
        print("Data Entered Sussefully")
    else:
        indesx = clintlist[n]
        file_path = f"fitnes_data/{indesx}_dite.txt"
        fileopen = open(file_path, "a")
        insertdataline = input("Enter Your Data :- ")
        fileopen.write(f"[ {gettimedata()} ] " + insertdataline + "\n")
        fileopen.close()
        print("Data Entered Sussefully")
while(1):
    for item in clintlist:
        print(f"For {clintindex} ",item)
        clintindex +=1

    clintname = int(input("Enter Your Clint Number :- "))

    worktype = input("Enter Your Work 1 : retrive  & 2 : inserdata : ")
    if(worktype=="1"):
        retrivedata((clintname-1))
    elif(worktype=="2"):
        insertdata((clintname-1))
    else:
        print("Please Chose Right Option")
    desgine = input("You Run This again [y/n] : ")
    if not(desgine=="y"):
        break
    else:
        clintindex = 1
