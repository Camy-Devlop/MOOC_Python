def antisymetrique(M):
    M2=[]
    if 0<len(M):
        for i in range(len(M)):
            m2=[]
            for j in range(len(M)):

                m2.append(-1*M[j][i])
            M2.append(m2)
        return M2
    else:
        return []
def print_mat(a):
    for i in a:
        t=""
        for ii in range(len(i)):
            t+=str(i[ii])+" "
        print(t)
    if len(a)==0:
        print()
m=[[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]
print_mat(m)
print()
print_mat(antisymetrique(m))
#[[4, 3, 8], [9, 5, 1], [2, 7, 6]]