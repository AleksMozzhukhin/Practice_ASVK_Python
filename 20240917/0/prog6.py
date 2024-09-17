while number := input():
    if eval(number) % 2 == 0:
        print(number)
    elif number == "13":
        print("Unlucky....")
        break
else:
    print("Congratulations!")
