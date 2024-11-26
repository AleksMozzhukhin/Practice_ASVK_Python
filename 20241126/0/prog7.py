import binascii

with open('random_file', "rb") as f:
    data = f.read()
res = binascii.hexlify(data, " ", 4).decode().split()
for addr, i in enumerate(range(0, len(res),4)):
    print(f"{addr:08x}", ":", *res[i:i+4])
