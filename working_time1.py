week = input("请输入星期：")
time = input("请输入时间：")

time_ranges = [
    "周一8:30到17:30",
    "周二8:30到17:30",
    "周三8:30到17:30",
    "周四8:30到17:30",
    "周五8:30到17:30"
]


def end_time(end_time: str):
    if end_time > "17:30":
        return "17:30"
    else:
        return end_time


time = end_time(time)

if week < "一" or week > "七":
    print("错误")
else:
    for i in range(week - 1):
        print(time_ranges[i], end=" ")
    print(f"周{week}8:30到{time}")
