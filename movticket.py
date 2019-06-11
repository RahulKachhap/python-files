firstclassavailable=3
secondclass=4
while(firstclassavailable!=0 or secondclass!=0):
    clas=int(input("press 1 for firstclass 2 for secondclass:"))
    '''if(clas!=1 and clas!=2):
        print("invalid choice")
    elif:'''
    tickets=int(input("how many tickets you need:"))
    #firstclass ticket available case
    if(clas==1 and tickets<=firstclassavailable and tickets<=firstclassavailable+secondclass):
        firstclassavailable-=tickets
        print("you have been issued %d firstclass Tickets"%(tickets))
    elif(clas==1 and tickets>firstclassavailable and tickets<=secondclass and tickets<=firstclassavailable+secondclass):
        print("sorry we have only %d firstclass,%d second tickets, please choose from these"%(firstclassavailable,secondclass))
        secondoption=int(input("press 1 for book available tickets of your choice and rest in other class, 2 for book all the tickets from the other class"))
        #case 1
        if(secondoption==1):
            otherclassticket=tickets-firstclassavailable
            secondclass-=otherclassticket
            print ("you have been issued %d firstclass and %d secondclass tickets"%(firstclassavailable,otherclassticket))
            firstclassavailable-=firstclassavailable
        #case 1
        elif(secondoption==2):
            secondclass-=tickets
            print("you have been issued %d second class tickets"%(tickets))
  
    #secondclass ticket available case
    if(clas==2 and tickets<=secondclass and tickets<=firstclassavailable+secondclass):
        secondclass-=tickets
        print("you have been issued %d secondclass Tickets"%(tickets))
    elif(clas==2 and tickets>secondclass and tickets<=firstclassavailable and tickets<=firstclassavailable+secondclass):
        print("sorry we have only %d firstclass,%d second tickets, please choose from these"%(firstclassavailable,secondclass))
        secondoption=int(input("press 1 for book available tickets of your choice and rest in other class, 2 for book all the tickets from the other class"))
        #case 1
        if(secondoption==1):
            otherclassticket=tickets-secondclass
            firstclassavailable-=otherclassticket
            print ("you have been issued %d secondclass and %d firstclass tickets"%(secondclass,otherclassticket))
            secondclass-=secondclass
        #case 1
        elif(secondoption==2):
            firstclassavailable-=tickets
            print("you have been issued %d first class tickets"%(tickets))
  
   
        
        
