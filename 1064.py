n=int(input())
arr=[]
years=[]
year=[]
#Append informations to array
for i in range(n):
    info=list(map(int,input().split()))
    arr.append(info)


#Append to array years of girls'
arren=list(enumerate(arr))
for j in arren:
    if j[1][1]==0:
        years.append(j)
    else:
        continue

if len(years)==0:
    print(-1)
else:
    for t in years:
        year.append(t[1][0])
    year.sort()
    small=year[0]
    for m in years:
        if m[1][0]==small:
            print(m[0]+1)
            break
        else:
            continue
     
    