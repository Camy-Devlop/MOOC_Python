from math import factorial
import matplotlib.pyplot as plt
def catalan(n):
    res=factorial(n)//((factorial(n+1))*factorial(n))
    return res

def get_espace(n, char):
    ligne = ""
    for i in range(n):
        ligne += char
    return ligne


def get_chiffre(debut, max):
    ligne = ""
    for i in range(debut, max):
        ligne += str(((i+1) % 10))

    for i in range(max, debut - 1, -1):
        ligne += str(((i+1) % 10))


    return ligne
cpt=9
#
print(get_espace(cpt, ' ')+str(1))
for i in range(1,10):
    print(get_espace(cpt-1, ' ')+get_chiffre(i,i*2))
    cpt-=1
#print(catalan(2))

x=range(1,10)
y=[8,3,4,3,9,3,5,4,3]
plt.plot(x,y)
