import readline
while s:=input('> '):
    match s.split():
        case["mov", r1,r2]:
            res=f"moving{r2} to {r1}"
        case [("push" | "pop") as cmd, *regs] if len(regs)>0:
            res=f"{cmd}with {r1}"
        case _:
            res= "Parse error"
    print(res)