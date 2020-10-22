def distance_mots(a, b):
    tab=list(a.strip())
    tabint=[]
    for i in a:
        tabint.append(ord(i))

    tabint=sorted(tabint)
    a="ae"

    for i in range(len(a)):
        tabint[i]=chr(tabint[i])
    print(tabint)
distance_mots("bonjour","")