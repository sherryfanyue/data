def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
file = open("content.txt", "w")
file.write(message)
file.close()


def increment(number, by):
    return number + by


print(increment(by=2, number=1))
