def check_cols(matrice):
    m=matrice
    test=0
    for i in range(len(m)):
        cpt=1
        print("--------------------")
        for j in range(len(m)):

            for jj in range(len(m)):
                if m[j][i]==jj+1:
                    print(m[j][i]," ",jj+1, cpt)
                    cpt += 1
                if cpt==9:
                    test+=1
    print(test)
    return test==81





d=[[1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 5, 1, 2, 3, 4, 9, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]]
for i in d:
    m=""
    for j in i:
       m+=str(j)+" "
    print(m)
f=check_cols(d)
print(f)