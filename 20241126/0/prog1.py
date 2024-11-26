with open("text") as f:
    data = f.read()
# print(data)
# for i in range(len(data)//3, len(data)):
t=data[len(data)//3+1:].find("\n")
print(data[:len(data)//3+t+1])