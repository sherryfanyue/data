week = int(input("请输入星期："))
time = input("请输入时间：")
a = str("周一8：30到17：30")
b = str("周二8：30到17：30")
c = str("周三8：30到17：30")
d = str("周四8：30到17：30")
e = str("周五8：30到17：30")


def end_time(end_time: str):
    if end_time > "17:30":
        return "17:30"
    else:
        return end_time


time = end_time(time)

if week < 2:
    print("周一8：30到", time)
if 2 <= week < 3:
    print(a, "周二8：30到", time)
if 3 <= week < 4:
    print(a, b, "周三8：30到", time)
if 4 <= week < 5:
    print(a, b, c, "周四8：30到", time)
if 5 <= week < 6:
    print(a, b, c, d, "周五8：30到", time)
if 6 <= week <= 7:
    print(a, b, c, d, e)
if week > 7:
    print("错误")
