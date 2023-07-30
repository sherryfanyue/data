class Computer:
    CPU = "7735H"
    memory = 0
    device = 0
    GPU = "4060"

    def __str__(self) -> str:
        return f"CPU是{self.CPU},显卡是{self.GPU}, 硬盘大小{self.device}G, 内存大小{self.memory}G"

