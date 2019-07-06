text = open("text.txt", 'r')
s = text.read().replace('\n', ' ').lower().split()
text.close()
s.sort()
x=[s[0]]
i=0
while i<(len(s)-1):
	if s.count(s[i])>s.count(x[0]):
		x[0]=s[i]
		i+=1
	else:
		i+=1
		continue
print(x)