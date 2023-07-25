student_count = 1000
rating = 4.99
is_published = True
course_name = "Python"
print(student_count)
message = """
Hi,

This is me
"""
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
course = "Python programming"
print(course)
first = "fanyue"
last = "meng"
full = f"{first} {last}"
print(full)
print(course.upper())
print(course.title())
print(course.strip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 ** 3)
print(round(2.9))
print(abs(-2.9))
x = input("x: ")
y = int(x) + 1
print(f"x:{x} y:{y}")
temperature = 35
if temperature > 30:
    print("it is warm")
elif temperature > 20:
    print("it is warm")
else:
    print("cold")
high_income = True
good_credit = True
if high_income and good_credit:
    print("eligible")
else:
    print("not eligible")

successful = False
for number in range(3):
    print("attempt", number)
    if successful:
        print("successful")
        break
else:
    print("failed")

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

command = ""
while command.lower() != "quit":
    command = input("> ")
    print("echo", command)
    
