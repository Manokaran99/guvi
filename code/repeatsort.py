n=int(input())
a=input().split()
arr=[]
y=[]
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
    if(a[i]==a[j]):
      arr.append(a[j])
y=sorted(arr)
for i in range(0,len(y),1):
  print(y[i],end=" ")
