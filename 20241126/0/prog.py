with open("text", "rb") as file:
    data = file.read()
with open("text", "wb") as file:
    file.write(data[len(data)//2+1:])
    file.write(data[:len(data)//2])
