def longueur(*points):
    res=0

    for i in range(len(points)-1):
        a=points[i]
        b=points[i+1]
        x1 = a[0]
        x2 = b[0]
        y1 = a[1]
        y2 = b[1]
        res+=((x1-x2)**2+(y1-y2)**2)**0.5
    return res


def my_insert(a, b):
    if isinstance(b,int):
        a.append(b)
        a.sort()
        tab=a
        return tab
    else:
        return None

#print(longueur((35.0, 20.0), (10.5, 27.0), (26.0, 0.0), (16.0, 33.0)))

print(my_insert([1, 3, 5], 4))