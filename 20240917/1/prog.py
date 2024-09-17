number =int(input())
print("A", end=" ")

if number%2==0 and number%25==0:
    print("+", end=" ")
else:
    print("-", end=" ")

print("B", end=" ")
if number%2!=0 and number%25==0:
    print("+", end=" ")
else:
    print("-", end=" ")

print("C", end=" ")
if number%8==0:
    print("+")
else:
    print("-")