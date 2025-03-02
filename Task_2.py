import random

a = random.randint(0,10)
b = random.randint(0,10)
print(f"a = {a}")
print(f"b = {b}")
if a == 0:
    if b == 0:
        print("Бесконечное множество решенйи")
    else:
        print("Нет решений")
else:
    x = -(b/a)
    print(f"x = {x}")