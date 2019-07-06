Result=[]
Start=[]
with open('input.txt','r') as inf:
    for s in inf:
       s=s.strip().split(';')
       Start.append(s)

sumMiddle = 0
for el in Start:
	el[1] = int(el[1])
	el[2] = int(el[2])
	el[3] = int(el[3])
for el in Start:
	sumMiddle = (int(el[1]) + int(el[2]) + int(el[3])) / 3
	print(round(sumMiddle, 9))
	#with open('out.txt','w') as ouf:
	    #ouf.write(str(round(sumMiddle, 9)))

Math, Physics, Russian = 0, 0, 0
for el in Start:
    Math += el[1]
    Physics += el[2]
    Russian += el[3]
Math /= len(Start)
Physics /= len(Start)
Russian /= len(Start)

print(round(Math, 9), round(Physics, 9), round(Russian, 9))
    #with open('out.txt', 'w') as ouf:
    	#ouf.write(round(Math, 9), round(Physics, 9), round(Russian, 9))