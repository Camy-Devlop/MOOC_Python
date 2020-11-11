d="dddsq sdqsdf\nffqfqd fqsdf\ndfs qdfqsdf"
dd=d.split('\n')

print(dd[0].strip(" "))

v=2674.72
r108=round(v*108/100,2)
print(r108)
print(round(r108*13.07/100,2))


import sys

sys.path.append("..")
dd="(3, 16), (\"En Python,  quel est le symbole d'affectation : = ou == ?\", \'=\')"

f=dd.split("),")

f[1]=f[1].split("\",")
f[0]=f[0].split(",").strip("(")
print(f[0])
for i in f[1]:
    print(i)
