class Bus:
    # connect RAM size of 64 KiB to bus
    ram: list[int] = [0] * 64 * 1024

    def __init__(self) -> None:
        pass

    def write(self, addr: int, data: int) -> None:
        # list of valid addresses for 6502 is 0x0000 - 0xffff
        if addr >= 0x0000 and addr <= 0xFFFF:
            self.ram[addr] = data

    def read(self, addr: int, read_only: bool = False) -> int:
        if addr >= 0x0000 and addr <= 0xFFFF:
            return self.ram[addr]
        return 0x00


# globally defined bus
BUS_6502 = Bus()
