import random
import re
flagy=0
def create_account():
    account=[]
    acc_no=random.randint(0,1000000000000000)
    acc_name=input("Enter your name:")
    check_acc_name(acc_name)
    acc_address=input("Enter your address:")
    check_acc_address(acc_address)
    acc_phonenumber=input("Enter phone number:")
    check_acc_phoneno(acc_phonenumber)
    acc_adhaarno=input("Enter adhaar number:")
    check_acc_adhaarno(acc_adhaarno)
    acc_panno=input("enter pan number:")
    check_acc_panno(acc_panno)
    
    account.append(acc_no)
    account.append(acc_name)
    account.append(acc_address)
    account.append(acc_phonenumber)
    account.append(acc_adhaarno)
    account.append(acc_panno)
    account.append(250)
    print("account created successfully")
    print(account)
    #appending the individual account to the existing accounts list
    accounts.append(account)


def check_acc_name(name):
    if re.match(r'^[A-Za-z\s]{1,30}$',name):
        pass
    else:
        print("Invalid input!!!Enter proper name")
       
        exit(0)
    
def check_acc_address(address):
    if re.match(r'^[A-Za-z\s]{1,50}$',address):
        pass
    else:
        print("Invalid input!!!Enter proper address")
        
        exit(0)
    
def check_acc_phoneno(phone):
    if re.match(r'^[0-9]{10}$',phone):
        pass
    else:
        print("Invalid input!!!Enter proper phone number")
        
        exit(0)
    
def check_acc_adhaarno(adhaar):
    if re.match(r'^[0-9]{12}$',adhaar):
        pass
    else:
        print("Invalid input!!!Enter proper adhaar number")
        
        exit(0)
    
def check_acc_panno(pan):
    if re.match(r'^[A-Z]{5}\d{4}[A-Z]$',pan):
        pass
    else:
        print("Invalid input!!!Enter proper PAN number")
        
        exit(0)

def display():
    print("Sl.No\tACC NO\t\t\tNAME\tADDRESS\t\tCONTACT NO\tADHAAR\t\tPAN NO\t\tBALANCE\n")
    for i in range(len(accounts)):
        print(i+1,"\t",accounts[i][0],"\t",accounts[i][1],"\t",accounts[i][2],"\t",accounts[i][3],"\t",accounts[i][4],"\t",accounts[i][5],"\t",accounts[i][6])
    print("\n")

def doDeposit():
    found=-1
    n=len(accounts)
    accnum=int(input("Enter your account number"))
    deposit=int(input("Enter the amount"))
    for i in range(n):
        if accounts[i][0]==accnum:
            accounts[i][6]=accounts[i][6]+deposit
            found=i
    print("Total bank balance now:",accounts[found][6]," rs")
    if found==-1:
        print("You have entered incorrect account number... please try again\n")

def doWithdraw():
    found=-1
    n=len(accounts)
    accnum=int(input("Enter your account number"))
    withdraw=int(input("Enter the amount"))
    for i in range(n):
        if accounts[i][0]==accnum:
            if withdraw<accounts[i][6]:
                accounts[i][6]=accounts[i][6]-withdraw
                print("Your current balance now : ",accounts[i][6])
                found=i
            else:
                print("LOW BALANCE!!\nYour balance is ",accounts[i][6],"rs")
    if found==-1:
        print("You have entered wrong account number\nplease try again")
        return 

def changeNumber():
    found=-1
    accountNumber=int(input("Enter your account number"))
    for i in range(len(accounts)):
        if accounts[i][0]==accountNumber:
            found=i
    if found==-1:
        print("Invalid account number")
        return
    print("Your present account number ",accounts[found][3])
    newPhonenumber=input("Enter new phone number")
    check_acc_phoneno(newPhonenumber)
    if newPhonenumber==accounts[found][3]:
        print("Do not enter old phone number as new number")
    accounts[found][3]=newPhonenumber
    print("Phone number edited successfully")


print("Welcome to ABC bank\n")
accounts=[]
while True:
    print("1.create account\n2.deposit\n3.Display\n4.withdraw\n5.Change number\n6.Exit\n")
    choice=int(input("Enter your choice:"))
    if choice==1:
        create_account()
    elif choice==2:
        doDeposit()
    elif choice==3:
        display()
    elif choice==4:
        doWithdraw()
    elif choice==5:
        changeNumber()
    elif choice==6:
        print("Exiting...\n")
        exit(0)
    else:
        print("Wrong input!!!")



