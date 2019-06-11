import csv


listobj=[]
with open("student.csv") as textfile:
    textreader=csv.reader(textfile)
    headers = next(textreader)
    for val in range(0,len(headers)):
        listobj.append({headers[val]:[]})
    print(listobj)

    for items in listobj:
        print(items)
        for values in textreader:
            listobj[items].append(values)
        print(listobj)
    '''for value in textreader:
        for items in value:
            listobj.append([value,[]])
            #print(listobj)
        #for items in value:
            #print(items[0])'''
