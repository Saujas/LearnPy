i,j,tmp = 0,0,0
list = [5,3,1,9,8,2,4]
for i in range(7):
    for j in range(i+1,7):
        if(list[i]>list[j]):
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp
print(list)