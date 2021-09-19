t=[20,10,20,10,20,10,20,10,20,10,20,10,20,10,20,10,20,10,20,10,20,10,20,10]
print(round(sum(t)/24,2))
print(min(t))
print(max(t))
tMax=[]
tMin=[]
for i in range(0,len(t)):
    if t[i]==max(t):
        tMax.append(i)
print("orele cu tMax: ",tMax)
for i in range(0,len(t)):
    if t[i]==min(t):
        tMin.append(i)
print("orele cu tMin: ",tMin)

