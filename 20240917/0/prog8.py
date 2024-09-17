match int(input()):
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case var if var % 2 == 0:
        print("Even")
    case var:
        print(var, "-- that's a lot..")
