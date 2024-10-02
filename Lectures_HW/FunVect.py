def superposition(funmode, funseq):
    ans=[]
    for i in funseq:
        def function_compress(x, j=i):
            return funmode(j(x))
        ans.append(function_compress)
    return ans