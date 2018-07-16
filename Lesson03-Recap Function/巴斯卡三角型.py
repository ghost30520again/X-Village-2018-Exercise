def f(n):
    
    pascalList=[]

#計算Pascal三角形的值
    for i in range(n):
        pascalList.append([])        
        pascalList[i].append(1)

        for j in range(1,i):
            pascalList[i].append(pascalList[i-1][j-1]+pascalList[i-1][j])
            
        if(n!=0):
            pascalList[i].append(1)

#輸出Pascal三角形
    for i in range(n):
        print("   "*(n-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:5}'.format(pascalList[i][j]),end=" ",sep=" ")
        print()

f(5)