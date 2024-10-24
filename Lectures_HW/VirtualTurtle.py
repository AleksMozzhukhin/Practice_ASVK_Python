def turtle(coord, direction):
    x, y = coord
    while action := (yield x, y):
        if action == "f":
            match direction:
                case 0:
                    x += 1
                case 1:
                    y += 1
                case 2:
                    x -= 1
                case 3:
                    y -= 1
        else:
            match action:
                case "l":
                    direction = (direction + 1) % 4
                case "r":
                    direction = (direction - 1) % 4
