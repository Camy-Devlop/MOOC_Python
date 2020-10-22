def soleil_leve(a,b,c):
    res=False #deux_egaux
    if a == b and a == 12:
        return False
    elif a == b and a == 0:
        return True
    elif c == a:
        return True
    else:
        if a<b and b<c:
            return False
        elif a<c and c<b:
            return True
        elif b<c and c<a:
            return False
        elif b<a and a<c:
            return True
        elif c<a and a<b:
            return False
        elif c<b and b<a:
            return True
        else:
            return False

for i in range(0,24):
    if soleil_leve(6,18,i)==soleil_leve(10,21,i):
        res=str(i)+" *"
    else:
        res = str(i)
    print(res)