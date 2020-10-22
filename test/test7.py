import os
def nouveaux_heros(a,b=""):

    nom_o=["Jacqueline", "Paul", "Pierre"]
    nom_new = ["Mathilde", "Tom", "Paul"]
    with open(a, encoding="UTF-8") as lecture:
        text=(lecture.read()).split(" ")

        for i in range(len(nom_o)):
            for ii in range(len(text)):
                if nom_o[i]==text[ii]:
                    text[ii]=nom_new[i]
        print(text)
    with open(b,'w', encoding="UTF-8") as ecriture:
        t=""
        for ii in text:
            t+=ii+" "
        print(t)
        ecriture.write(t)

nouveaux_heros("./test.txt","./nouvelle_histoire_1.txt")