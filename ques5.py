a=[]
for i in range(3):
	a.append([])
	for j in range(3):
		a[i].append(int(input()))
print(a)
c=[]
for i in range(3):
	c.append([])
	for j in range(3):
		c[i].append(int(input()))
print(c)
b=[]
for i in range(3):
	b.append([])
	for j in range(3):
		b[i].append(0)

for i in range(3):
	for j in range(3):
		for k in range(3):
			b[i][j]+=a[i][k]*b[k][j]
print(b)


