point = dict(x=1, y=2)
point["a"] = 20
point["x"] = 10
print(point.get("a", 0))
del point["x"]
print(point)
for 键,值 in point.items():
    print(键,值)
