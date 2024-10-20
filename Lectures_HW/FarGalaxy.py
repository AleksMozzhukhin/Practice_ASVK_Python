dictionary={}
while s:=input():
    if len(s)<2:
        break
    dictionary[tuple(map(float, s.split()[:3]))]=s.split()[-1]

distanses=[]
tmp=list(dictionary.items())
for i in range(len(tmp)):
    for j in range(i+1,len(tmp)) :
            distanses.append((((tmp[i][0][0]-tmp[j][0][0])**2+(tmp[i][0][1]-tmp[j][0][1])**2+(tmp[i][0][2]-tmp[j][0][2])**2), (tmp[i][1], tmp[j][1])))
maximum=max(distanses, key=lambda x: x[0])
print(*sorted(maximum[1]))