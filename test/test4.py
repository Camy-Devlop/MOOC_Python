def duree(a, b):
    res = 0
    if a[0] < b[0]:
        t1 = a[0] * 60 + a[1]
        t2 = b[0] * 60 + b[1]
        res = ((t2 - t1) // 60, int(round((((t2 - t1) / 60) - ((t2 - t1) // 60)) * 60,0)))
        print("ttt ", round((((t2 - t1) / 60) - ((t2 - t1) // 60)) * 60,0))
        return res
    else:
        t1 = a[0] * 60 + a[1]
        print("t1",t1)
        t2 =(24 * 60)+ b[0] * 60 + b[1]
        print("t2", t2)
        res = ((t2 - t1) // 60, int(round((((t2 - t1) / 60) - ((t2 - t1) // 60)) * 60,0)))

        return res
print(duree((9, 33), (13, 50)))