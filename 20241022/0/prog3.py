def pgen():
    print("::")
    print("Before")
    res = yield "Start"
    print(">")
    while res := (yield f"/{res}/"):
        print(">>")
    yield "Finish"
    print("<")


g = pgen()
# s = next(g)
# print(s)
# s = g.send("!%$^##")
# print(s)
# s = g.send("1234")
# print(s)
print(next(g))
for c in range(6, -1, -1):
    print(g.send(c))