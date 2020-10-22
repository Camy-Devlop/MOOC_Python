def rac_eq_2nd_deg(a, b, c):
    if (b)**2-4*a*c<0:
        return tuple()
    elif  (b)**2-4*a*c==0:
        return ((-b)/(2*a),)
    elif  (b)**2-(4*a*c)>0:
        delta=((b)**2)-(4*a*c)
        x1=((-b-(delta**0.5))/(2*a))
        x2=((-b+(delta**0.5))/(2*a))
        res=[x1,x2]
        res.sort()
        return (res[0],res[1])
print(rac_eq_2nd_deg(-1.0,8.0,-1.0))
