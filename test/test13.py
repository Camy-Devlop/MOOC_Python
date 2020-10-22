def aa(dico: dict):
    res = set(dico.keys())
    res2 = []

    for i in range(2):
        candi = ""
        a = 0
        for can in res:
            if a < dico[can]:
                a = dico[can]
                candi = can
                print(candi)

        res -= {candi}
        res2.append(candi)
        print(res)


aa({'Candidat 7': 2,
    'Candidat 2': 38,
    'Candidat 6': 85,
    'Candidat 1': 8,
    'Candidat 3': 17,
    'Candidat 5': 83,
    'Candidat 4': 33})
f = [4, 5, 6, 7]
ss = set()
for i in f:
    ss.add(i)
sss = tuple(ss)
print(sss)
print("--------------------------------------")
d = {}
b = 4.5
d[1] = 22
d[3.14] = 24
d[(3, 4)] = 32
d[2] = (3, 4)
d[5, 4] = [5, 4]
print(b, d)

print("--------------------------------------")


def substitue(message, lecique):
    m = message.split(" ")
    m_new = ""
    for i in m:
        if i in lecique.keys():

            m_new += lecique[i] + " "
        else:
            m_new += i + " "
    print(m_new)


substitue('C. N. cpt 2 to inf', {'C.': 'Chuck',
                                 'N.': 'Norris',
                                 'cpt': 'counted',
                                 '2': 'two times',
                                 'inf': 'infinity'})
print("--------------------------------------")
import os


def nouveaux_heros(a):
    sepa = "!§?:.,;\'\"\t\n-_ "
    text = ""
    ligne = 0
    mots = 0
    nb_char = 0
    tab=[]
    tmp=""
    with open(a, "r", encoding="utf-8") as lecture:
        text = lecture.read()

    for i in text:
        if i not in sepa:

            if i.isalnum() == True:
                tmp += i
        else:
            if tmp.isalnum():
                tab.append(tmp)
                tmp = ""

    print(text)
    print(tab)
    mots=len(tab)
    ligne = text.count("\n")
    nb_char = len(text)
    print(nb_char,mots, ligne)


nouveaux_heros("le-petit-prince.txt")
sepa = "!§?:.,;\'\"\t "
m=""

cpt=0
tmp=""
tab=[]
for i in m:
    if  i not in sepa:
      if i.isalnum()==True:
        tmp+=i
    else:
        if tmp.isalnum():
            tab.append(tmp)
            tmp=""
cpt=len(tab)
print(tab,cpt)

print("--------------------------------------")
def liste_des_mots(adress):
    text = ""
    res = set()
    res2 = []
    p = "-\'\"\n\t?!:;.,*=()1234567890"
    with open(adress, "r", encoding="utf-8") as lecture:
        text = lecture.read()
        text = text.lower()
        for i in p:
            text = text.replace(i, " ")

    res = set(text.split(" "))
    for i in res:
        if i != "":
            res2.append(i)
    res2.sort()
    return res2
print(liste_des_mots("le-petit-prince.txt"))
