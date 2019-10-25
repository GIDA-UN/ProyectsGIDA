#f=open ('test.txt','r')
#data = f.readlines()
#print(int(data)*2)

with open('test.txt') as f:
    data = f.read().splitlines() 
dataFloat=[]
count=1
for i in data:
    dataFloat.append(float(i))
print(dataFloat)
f.close()

