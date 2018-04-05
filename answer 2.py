num=int(input())
strlist=[]
strlist=strlist.append(num)
numlist=[]
numlist=numlist.append(num)
for i in (n):
    strlist=strlist.append(input())
for j in range(1,(num+1)):
    if strlist[j]=='a':
        numlist=numlist.append(1)
    elif strlist[j]=='b':
        numlist=numlist.append(2)
    elif strlist[j]=='c':
        numlist=numlist.append(3)    
    elif strlist[j]=='d':
        numlist=numlist.append(4)    
    elif strlist[j]=='e':
        numlist=numlist.append(5)
    elif strlist[j]=='f':
        numlist=numlist.append(6)
    elif strlist[j]=='g':
        numlist=numlist.append(7)

    elif strlist[j]=='h':
        numlist=numlist.append(8)
    elif strlist[j]=='i':
        numlist=numlist.append(9)
    elif strlist[j]=='j':
        numlist=numlist.append(10)
    elif strlist[j]=='k':
        numlist=numlist.append(11)
    elif strlist[j]=='l':
        numlist=numlist.append(12)
    elif strlist[j]=='m':
        numlist=numlist=numlist.append(13)
    elif strlist[j]=='n':
        numlist=numlist.append(14)
    elif strlist[j]=='o':
        numlist=numlist.append(15)
    elif strlist[j]=='p':
        numlist=numlist.append(16)
    elif strlist[j]=='q':
        numlist=numlist.append(17)
    elif strlist[j]=='r':
        numlist=numlist.append(18)
    elif strlist[j]=='s':
        numlist=numlist.append(19)
    elif strlist[j]=='t':
        numlist=numlist.append(20)
    elif strlist[j]=='u':
        numlist=numlist.append(21)
    elif strlist[j]=='v':
        numlist=numlist.append(22)
    elif strlist[j]=='w':
        numlist=numlist.append(23)
    elif strlist[j]=='x':
        numlist=numlist.append(24)
    elif strlist[j]=='y':
        numlist=numlist.append(25)
    else:
        numlist=numlist.append(26)

for k in range(1,num):
    a_k=0
    for l in range((k+1),(num+1)):
         if numlist[k]>numlist[l]:
             a_k=a_k+1
for k in range(1,(num-1)):
    fac_k=1
    for m in range(1,(num-k)):
        fac_k=fac_k*m
for k in range(1,num):
    ans=a_k*fac_k
print(ans+1)    
    
        
             
             
        
    
        