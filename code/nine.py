N=int(input())
K=int(input())
arr=[]
sum=0
for i in range(N):
  n=int(input())
  arr.append(n)
for j in range(K):
  sum=sum+arr[j]
print(sum)
