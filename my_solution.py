import sys
z=[]
for i in sys.argv:
	z.append(i)
del z[0]
print(*z)