def premier(a):
    a,m=a,a
    t=[]
    while 1<=m:
        if 1<=m:
            tmp=[]
            for i in range(1,a):
                if m%i==0:
                    tmp.append(m)
            if len(tmp)==1:
                t.append(tmp[0])
        m-=1
    t.sort()
    test =False
    for i in t:
        if a==i:
            test=True
    return test
n=37
if n!=1:
    mm=""
    for ii in range(n):
        if premier(ii):
            mm+=str(ii)+" "

    print(mm)