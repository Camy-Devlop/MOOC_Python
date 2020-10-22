def antisymetrique(M):
    M2 = []
    test = True
    if 0 < len(M):
        for i in range(len(M)):
            m2 = []
            for j in range(len(M)):
                m2.append(-1 * M[j][i])
            M2.append(m2)

        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == M2[i][j]:
                    test *= True
                else:
                    test *= False
        return test
    else:
        return test

m=[[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]
print(antisymetrique(m))
s = [1,2,3,4,5,6,7]
print(s)
print()
#s[len(s):len(s)] = [0]
#print(s)
#s.extend([0])
#s.insert(len(s),9)
#s[0:1] = []
#del s[-len(s)]
s[len(s)-1:] = []
print(s)