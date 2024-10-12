def squares(w, h, *args):
    ans= [['.' for i in range(w)] for j in range(h)]
    for i in args:
        for q in range(i[0], i[2]+i[0]):
            for e in range(i[1], i[2]+i[1]):
                ans[e][q]=i[3]
    for i in ans:
        print(*i, sep="")
