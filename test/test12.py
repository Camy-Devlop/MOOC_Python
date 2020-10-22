import io
import ssl

import urllib3 as p
#import requests
#from urllib import *
##def p(x):
#    converter = lambda x : x*2 if x < 10 else (x*3 if x < 20 else x)
#    return converter(x)

def liste_des_mots(adress:str):

    #nom="Zola.txt"
    #req=requests.get(adress)
    #print(req.content)
    context = ssl._create_unverified_context()
    http = p.PoolManager()
    r = http.request('POST', adress, preload_content=False,verify=False,context)
    r.auto_close = False
    for line in io.TextIOWrapper(r):
        print(line)



    #

    #reponce=http.request("GET",adress)#.request("GET",adress)
    #print(reponce.status)
    #print(reponce.data)
    #print(reponce.data)
liste_des_mots("https://upylab.ulb.ac.be/pub/data/Zola.txt")

            #'http://httpbin.org/robots.txt')
            #"https://upylab.ulb.ac.be/pub/data/Zola.txt","Zola.txt")
               #"http://www.math.univ-toulouse.fr/~besse/Wikistat/pdf/st-intro.pdf","st-intro.pdf")