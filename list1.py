items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),

]


def sort_items(item):
    return item[1]


prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]
print(prices, filtered)

list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))
