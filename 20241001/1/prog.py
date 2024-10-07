def Pareto(*args):
    ans=[]
    for i in args:
        if all(not (i[0] <= j[0] and i[1]<=j[1] and (i[0]<j[0] and i[1]<j[1])) for j in args):
            ans.append(i)
    return tuple(ans)
print(Pareto((1,2), (3,4), (2,2), (4,3), (7,0), (1,8)))