def prime_numbers(a):
    tab = []
    t = 1
    m = 1
    cpt = 0
    if 0 < a:
        while len(tab) != a:
            tmp = []
            for i in range(1, t):
                if m%i==0:
                    tmp.append(m)
            if len(tmp) == 1:
                tab.append(tmp[0])
            m += 1
            t += 1
        tab.sort()
        return tab
    else:
        if a == 0:
            return list()

        else:
            return None


print(prime_numbers(7))