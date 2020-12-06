def words_by_length(file):
    dico={}
    tmp:str
    with open(file,"r",encoding="utf-8") as lec:
        for i in lec:
            tmp=i
            tmp=tmp.lower()
        for p,j in enumerate(tmp):
            if j in "\'":
                tmp=tmp.replace("\'"," ",1)
            elif j in ".,?!-":
                tmp=tmp.replace(j," ",1)
        print(tmp)


        tmp=tmp.strip("\n")
        tmp=tmp.strip(" ")
        tmp=tmp.split(" ")

        for ii in tmp:
            if len(ii) not in dico.keys():
                dico[len(ii)]=set()
                dico[len(ii)].add(ii)
            else:
                dico[len(ii)].add(ii)
    dico.pop(0)
    dico2={}
    for i in range(1,len(dico)+1):
        dico2[i]=sorted(dico[i])

    return dico2

print(words_by_length("Zola.txt"))