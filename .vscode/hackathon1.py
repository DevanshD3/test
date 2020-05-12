test=int(input())
sum1=[]
for i in range(test):
    sum=0
    c=0
    boxno=int(input())
    size=list(map(int,input().split()))
    for k in size:
        c=c+1
        for j in range(c):
            if size[j]<k:
                sum=sum+size[j]
    sum1.append(sum)

for i in sum1:
    print(i)