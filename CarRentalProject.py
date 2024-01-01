import os
from prettytable import PrettyTable
import time
from os.path import isfile

#Invoice related
def addInvoiceToFile(info):
    text = ""
    for item in info:
        text+=str(item)
        text+=","
    text= text.rstrip(",")
    text+="\n"
    with open("invoice.txt","a+") as file:
        file.write(text)
    file.close()

def displayInvoice(info):
    os.system("cls")
    print(f"\tINVOICES\n---------------------------------\n")
    for index in range(4):
        print(f"{InvoiceHeaders[index]}:\t{info[index]}")
    print("---------------------------------")
    os.system("pause")
    HomePage()


def Invoice(name, info, saveData=True):
    os.system("cls")
    print(f"\tYOUR INVOICE\n---------------------------------\n")
    for i in range(2,len(InvoiceHeaders)):
        userinput = input(f"{InvoiceHeaders[i]}:\t")
        info.append(userinput) 
    if saveData == True:
        addInvoiceToFile(info)
    displayInvoice(info)


def Invoices():
    os.system("cls")
    data = readData("invoice.txt")
    if data != []:
        for rowindex in range(len(data)):
            print(f"\tINVOICES\n---------------------------------\n")
            for index in range(4):
                print(f"{InvoiceHeaders[index]}:\t{data[rowindex][index]}")
            print("---------------------------------")
        os.system("pause")
        HomePage()
    else:
        print("There's no record yet!")
        time.sleep(4)
        HomePage()

#Making The Table
def MakeTable(Headers,fileName):
    Data = readData(fileName)
    table = PrettyTable(Headers)
    table.add_rows(Data)
    return table

#reading the data from a file
def readData(fileName):
    with open(fileName,"r") as file:
        data = file.readlines()
    file.close()
    datalist = []
    for row in data:
        item = row.split(",")
        if item[-1] == "\n":
            item.pop()
        item[-1]=item[-1].rstrip("\n")
        datalist.append(item)
    return datalist

#selecting an option from the homepage
def selectChoice():
    os.system("cls")
    CarList = readData("carlist.txt")
    print(MakeTable(CarListHeaders, "carlist.txt"))
    choice = int(input("Press 0 for Back...\nYour Choice: "))
    if choice == 0:
        HomePage()
    else:
        while choice > len(CarList):
            print("Invalid number")
            choice = int(input("Your Choice: "))
        info=[name,CarList[choice-1][1]]
        if int(CarList[choice-1][4]) > 0:
            CarList[choice-1][4] = str(int(CarList[choice-1][4])-1)
            saveData("carlist.txt",CarList)
            Invoice(info[0], info, True)
        else:
            os.system("cls")
            print("No car left in storage")
            os.system("pause")
            HomePage()
        
        
        os.system("cls")
    # print(f"\tINFORMATION\n----------------------------------------------\nName:\t{name}\nCar:\t{CarList[choice-1][1]}\t")
    # for index in range(2,len(InvoiceHeaders)):
    #     nInfo=input(f"{InvoiceHeaders[index]}:\t")
    #     info.append(nInfo)
    
    # Invoice(name,info,saveData=True)
    
    

#converting a list to a text 
def getReadyForBeingWritten(nData):
    text = ""
    for row in nData:
        line = ""
        for item in row:
            line+=str(item)
            if row.index(item) != len(row)-1:
                line+=","
        text+=line
        text+="\n"
    return text


#saving the data to a file
def saveData(fileName,Data):
    dataText = getReadyForBeingWritten(Data)
    with open (fileName,"w")as file:
        file.writelines(dataText)
        file.close()

#creating a file if it does not exist
def createFileIfNotExist(fileName,Data):
    if not isfile(fileName):
        with open(fileName, "w")as file:
            file.close()
        saveData(fileName,Data)


#adding a car to the carlist
def AddInformation():
    os.system("cls")
    nCar = []
    CarList = readData("carlist.txt")
    with open("carlist.txt","r")as f:
        num = len(f.readlines())
    nCar.append(num+1)
    print("Enter the new car's information: ")
    for i in range(1,len(CarListHeaders)):
        print(CarListHeaders[i],": ")
        nInfo= input()
        nCar.append(nInfo)
    
    CarList.append(nCar)
    
    saveData("carlist.txt",CarList)
    HomePage()

#Editing the Quantity and Price
def EditInformation():
    os.system("cls")
    print(MakeTable(CarListHeaders,"carlist.txt"))
    CarList = readData("carlist.txt")
    edChoice = int(input("Enter the number of the car you want to edit: "))
    while edChoice > len(CarList):
        print("Invalid number")
        edChoice = int(input("Enter the number of the car you want to edit: "))
    os.system("cls")
    print("1\tPrice\n2\tQuantity")
    edSelect = int(input("Select what you want to edit: "))
    os.system("cls")
    if edSelect == 1:
        CarList[edChoice-1][2] = input("Enter new price: ")
    elif edSelect == 2:
        CarList[edChoice-1][4] = input("Enter new quantity: ")
    else:
        print("Invalid number")
    saveData("carlist.txt",CarList)
    os.system("cls")
    HomePage()


#deleting cars from the carlist        
def DeleteInformation():
    os.system("cls")
    print(MakeTable(CarListHeaders,"carlist.txt"))
    delChoice = int(input("Enter the number of the car you want to delete: "))
    CarList = readData("carlist.txt")
    while delChoice > len(CarList):
        print("Invalid number")
        delChoice = int(input("Enter the number of the car you want to delete: "))
    CarList.pop(delChoice-1)

    for rowIndex in range(delChoice-1, len(CarList)):
        CarList[rowIndex][0]= str(int(CarList[rowIndex][0])-1)

    saveData("carlist.txt",CarList)
    HomePage()

#Admin page
def Admin():
    adminPass = input("Password: ")
    if adminPass == "adminadmin" or adminPass == "12345678":
        os.system("cls")
        choice= input("""\tADMIN
        --------------------------------------------
        Select your choice:
        1\tAdd information
        2\tEdit information
        3\tDelete information
        4\tExit
        YOUR CHOICE: """)
        if choice.strip() == "1":
            AddInformation()
        elif choice.strip() == "2":
            EditInformation()
        elif choice.strip() == "3":
            DeleteInformation()
        elif choice.strip() == "4":
            os.system("cls")
            HomePage()
    else:
        os.system("cls")
        print("Wrong Password!")
        os.system("cls")
        HomePage()

#Home page
def HomePage():
    os.system("cls")
    choice = input("""
    MENU
    1 - Car List
    2 - Check Your Invoice
    3 - Admin Panel
    4 - Exit
    Your Choice: """)
    os.system("cls")
    if choice.strip() == "1":
        selectChoice()
    elif choice.strip() == "2":
        Invoices()
    elif choice.strip() == "3":
        Admin()
    elif choice.strip()=="4":
        print("GoodBye!")
        time.sleep(3)
        os.system("cls")
        exit()


def main():
    #gettin the username
    global name
    name= input("Please enter your name: ")
    os.system("cls")
    createFileIfNotExist("invoice.txt","")
    createFileIfNotExist("carlist.txt",CarList)

    HomePage()

#Car List
global CarListHeaders
CarListHeaders= [" ","Item Name","Price","Seat","Quantity"]
global CarList 
CarList = [[1,"Ford Fiesta",120,4,8],
           [2,"Mazda2",100,4,10],
           [3,"Audi A4",200,4,3],
           [4,"Leus Ls",210,5,4],
           [5,"Cadillac CTS",260,4,3],
           [6,"Porsche 911",400,2,2],
           [7,"BMW Z4",300,2,5],
           [8,"Mazda CX_3",120,5,12],
           [9,"Hyundai Santa Fe",120,5,10],
           [10,"Toyota Camry",100,4,10]]

global InvoiceHeaders
InvoiceHeaders = ["Name","Car","Number of Days","Rent Date"]
os.system("cls")
main()

