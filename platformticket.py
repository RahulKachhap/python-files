#platform ticket generator
import random
from datetime import datetime,timedelta
tickets={}
def issue():
    global issue_time
    id_no=random.randint(1111,9999)
    issue_time=datetime.now()
    tickets.update({id_no:issue_time})
    print(tickets)
def collector():
    print("please show your ticket..")
    ticket_id=int(input("ticket id:"))
    check_date=tickets[issue_time]+datetime.timedelta(minutes=15)
    print(check_date)
    
while(1):
    print("select type press 1 for issuer and 2 for collector:")
    choice=int(input("select your choice:"))
    if(choice==1):
        print("you choose for issuing ticket..")
        issue()
    elif(choice==2):
        print("you choose for collecting ticket..")
        collector()
    else:
        print("invalid choice..")
