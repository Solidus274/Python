import requests
with open ('dataset_3378_3.txt') as inf:
    file=inf.readline().strip()
r=requests.get(file)
while True:
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)    
    print(r.text)
    

