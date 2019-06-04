numb=int(input())
count=0
while(numb>0):
    dig=numb/10
    count=count+1
    numb=numb//10
print(count)
