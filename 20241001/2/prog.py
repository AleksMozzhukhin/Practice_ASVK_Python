def sub_upgrade(a, b):
    if isinstance(a, (list, tuple)):
        a=filter(lambda x: x not in b, a)
        if isinstance(a, list):
            return list(a)
        else:
            return tuple(a)
    else:
        return a - b


print(sub_upgrade(["Q", "WE", "RTY"], ["WE", "ZZ"]))
