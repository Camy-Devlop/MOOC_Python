d=[	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[2, 3, 4, 5, 6, 7, 8, 9, 1],
	[3, 4, 5, 6, 7, 8, 9, 1, 2],
	[4, 5, 6, 7, 8, 9, 1, 2, 3],
	[5, 6, 7, 8, 9, 1, 2, 3, 4],
	[6, 7, 8, 9, 1, 2, 3, 4, 5],
	[7, 8, 5, 1, 2, 3, 4, 9, 6],
	[8, 9, 1, 2, 3, 4, 5, 6, 7],
	[9, 1, 2, 3, 4, 5, 6, 7, 8]]
def check_cols(m):
	tcpt:dict={}
	numb : int
	dico:dict
	for i in range(len(m)):
		fois:int=0
		pos :tuple
		dico={}
		for j in range(len(m)):
			numb=m[j][i]
			pos=(i,j)
			if i not in tcpt.keys():
				fois+=1
				dico=dict()
				dico[m[j][i]]=[fois,[pos]]
				tcpt[i]=dico
			else:
				if numb in dico.keys():
					dico[numb][0]+=1
					dico[numb][1].append((i,j))
				else:
					dico[numb]=[1,[(i,j)]]
	test=True
	for c,i in tcpt.items():
		for cc,j in i.items():
			if j[0]>1:
				test=False
				break
		if test==False:
			break

	return test

t=check_cols(d)
print(t)