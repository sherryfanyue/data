def mutiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(mutiply(2, 3, 4, 5))


def save(**user):
    print(user["name"])


save(id=1, name="john", age=22)
