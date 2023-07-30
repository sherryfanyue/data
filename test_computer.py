from Computer import Computer

my_pc = Computer()
my_pc.device = 1024
my_pc.memory = 32

print(my_pc.__str__())

print(f"CPU是{my_pc.CPU},显卡是{my_pc.GPU}, 硬盘大小{my_pc.device}G, 内存大小{my_pc.memory}G")
