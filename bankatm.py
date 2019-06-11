import random

#registration for a bankaccount

def registration():
    global deposit,pin,accountno
    name=input("enter your name:")
    adharid=int(input("enter your adharid:"))
    phoneno=int(input("enter your phoneno:"))
    deposit=int(input("enter how much money you want to deposit"))
    #if(len(adharid)!=12):
    print("invalid adharid...agin input adharid correct")
    adharid=int(input("enter your adharid:"))
    #elif(len(phoneno)!=10):
    print("invalid phoneno...agin input phoneno correct")
    phoneno=int(input("enter your adharid:"))
    #else:
    print("successfully opened a bank account...")
    print("please note your bank account number and pin mentioned below..")
    accountno=random.randint(100000000000,999999999999)
    pin=random.randint(1000,9999)
    print("your account number is:",accountno)
    print("your pin is:",pin)

#withdrawl of money

def withdraw():
    global deposit,pin,accountno,inputpin,bankaccno,withdrawl
    bankaccno=int(input("enter your bankaccount number:"))
    if(bankaccno==accountno):
        withdrawl=int(input("enter how much money you want to withdraw:"))
        if(withdrawl<=deposit):
            inputpin=int(input("enter your pin:"))
            if(inputpin==pin):
                print("successfully withdrawl money %d"%(withdrawl))
                deposit-=withdrawl
                print("your updated balace is %d"%(deposit))
            else:
                print("invalid pin.")
        else:
            print("sorry you dont have enough balance to withdraw..")
    else:
        print("invalid bankaccountno enter valid account number")
#check balance

def checkbalance():
    global deposit,pin,accountno,inputpin1,bankaccno1
    bankaccno1=int(input("enter your bankaccount number:"))
    if(bankaccno1==accountno):
        inputpin1=int(input("enter your pin:"))
        if(inputpin1==pin):
            print(deposit)
        else:
            print("invalid pin.")

while(1):
    print("*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*")
    print("welcome to atm..")
    print("we can perform below mentioned functions for you please choose..")
    print("1.registration 2.withdrawl 3.check balance")
    print("*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*\n")
    choice=int(input("enter your choice:"))
    if(choice==1):
        print("you opted for registration..\n")
        registration()
    elif(choice==2):
        print("you opted for withdrawl..\n")
        withdraw()
    elif(choice==3):
        print("you opted for check balance..\n")
        checkbalance()
    else:
        print("invalid option")
        break
