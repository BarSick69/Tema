zi=["L","Ma","Mi","J","Vi","S","D"]
V=[]
for i in range(0,len(zi)):
    x=input("dati salariul de: {} ".format(zi[i]))
    V.append(int(x))
print("Salariul in fiecare zi: {}".format(V))
print(sum(V))
print(round(sum(V)/7,2))
print(max(V))
vMax=[]
vMin=[]
for i in range(0,len(zi)):
    if V[i]==max(V):
        vMax.append(zi[i])
print(vMax)
for i in range(0,len(zi)):
    if V[i]==min(V):
        vMin.append(zi[i])
print(vMin)
