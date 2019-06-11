def possiblespilt(length):
    options=[]
    print(length)
    for v in range(length):
        options.append([v,length-v])
    return options


number=[1,2,1,2,1]
spilt = possiblespilt(len(number))

result = []
print(spilt)
for option in spilt[2:3]:
    res = []
    for val in option:
        add = 0
        print("val-",val)
        if(option.index(val) == 0):
            for num in number[0:val]:
                add+=num
        elif(option.index(val) == 0):
            for num in range(number[val:]):
                add+=num
        res.append(add)
    result.append(res)
print(result)
