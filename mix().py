import random
lista=["Henrique", "Gian", "Mateus", "André", "Leonardo", "Carlos", "Felipe", "Ricardo"]
n=7
def mix(lista, n):
	c=1
	while len(lista)>0:
		grupo=[]
		if len(lista)<n:
			n=len(lista)
		for k in range(0, n):
			e=random.choice(lista)
			lista.remove(e)
			grupo.append(e)
		print("Grupo {}: {}".format(c, grupo))
		c=c+1
mix(lista, n)
