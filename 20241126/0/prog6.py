import random, struct

with open("random_file", "wb") as f:
    for i in range(10):
        f.write(struct.pack("f3si", random.random(), bytes([random.randrange(0, 256) for j in range(3)]),
                            random.randint(-128, 128)))

