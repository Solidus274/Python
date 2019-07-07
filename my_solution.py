import sys
z=[]
for i in sys.argv:
	z.append(i)
del z[0]
print(*z)






 r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/675.txt')
 print(requests.get(<https://stepic.org/media/attachments/course67/3.6.2/675.txt>).text)
import requests
with open ('dataset_3378_2.txt') as inf:
    file=inf.readline()
r=requests.get(file)