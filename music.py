MusicLibrary={"s1":{"artist":"abc","genre":"sad","singer":"arrahman","composer":"c1"}
              ,"s2":{"artist":"kbc","genre":"happy","singer":"arrahman","composer":"c2"}}
dataList=[]

for keys in MusicLibrary:
    tempList=MusicLibrary[keys].keys()
print(tempList)
for values in tempList:
    dataList.append({values:{}})
print(dataList)

for index in range(0,len(dataList)):
    print(index)
    for key in dataList[index]:
        print(key)
        for songs in MusicLibrary:
            print(songs)
