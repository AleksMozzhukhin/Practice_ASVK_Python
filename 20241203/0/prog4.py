from re import match

t = "qwreqw ewqr"
match t.split():
    case []:
        print("empty")
    case ["qwe"]:
        print("No doubt qwe")
    case [str(x)]:
        print("List fo 1 str")
    case [x]:
        print("List of 1")
    case [_, *tail]:
        print("List with tail", tail)
