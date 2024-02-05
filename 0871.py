n=int(input())
arr=[]
s=1
for i in range(1,i+1):
    arr.append(i)
for j in arr:
    if j%2==0:
        s+=j
    else:
        s-=j
if s%2==0:
    print("Jahongir")
else:
    print("Azizxon")