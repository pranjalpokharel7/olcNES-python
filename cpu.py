from enum import UNIQUE, IntFlag, verify

from bus import BUS_6502


class CPU6502:
    def __init__(self) -> None:
        pass

    @verify(UNIQUE)
    class Flags6502(IntFlag):
        C = 1 << 0  # carry bit, 0000 0001
        Z = 1 << 1  # zero, 0000 0010
        I = 1 << 2  # disable interrupts, 0000 0100
        D = 1 << 3  # decimal mode, 0000 1000
        B = 1 << 4  # break, 0001 0000
        U = 1 << 5  # unused, 0010 0000
        V = 1 << 6  # overflow, 0100 0000
        N = 1 << 7  # negative, 1000 0000

    # instruction set
    class Instruction6502:
        name: str
        op_func: function  # reference to the function that is called for the opcode
        am_func: function  # reference to the function that is called for address mode
        cycles: int  # number of cycles required for the instruction

    # instruction set is a 16 * 16 matrix which we store in a flat format
    instruction_set: list[Instruction6502] = (
        [Instruction6502()] * 16 * 16
    )

    # registers
    accumulator: int = 0x00
    x_reg: int = 0x00
    y_reg: int = 0x00
    pc: int = 0x00
    sp: int = 0x00
    status: int = 0x00

    # variables to store internal states
    fetched: int = 0x00
    addr_abs: int = 0x0000  # address used for addressing mode
    addr_rel: int = (
        0x0000  # address stored temporarily for jump instructions
    )
    opcode: int = 0x00  # opcode currently being executed
    cycles: int = (
        0  # cycles elapsed for the duration of the instruction
    )

    # clock
    def clock(self) -> None:
        pass

    # reset
    def reset(self) -> None:
        pass

    # interrupt request signal
    def irq(self) -> None:
        pass

    # non-maskable interrupt request
    def nmi(self) -> None:
        pass

    # read write from bus
    def read(self, addr: int) -> int:
        return BUS_6502.read(addr=addr)

    def write(self, addr: int, data: int) -> None:
        return BUS_6502.write(addr=addr, data=data)

    # get and set flags
    def get_flag(self, flag: Flags6502) -> None:
        pass

    def set_flag(self, flag: Flags6502, v: bool) -> None:
        pass

    # internal functions
    def fetch(self) -> int:
        """Fetch data for internal functions."""
        return 0

    # addressing modes
    def am_imp(self) -> int:
        """Implied addressing mode."""
        return 0

    def am_imm(self) -> int:
        """Immediate addressing mode."""
        return 0

    def am_zp0(self) -> int:
        """Zero page addressing mode."""
        return 0

    def am_zpx(self) -> int:
        """Zero page X addressing mode."""
        return 0

    def am_zpy(self) -> int:
        """Zero page Y addressing mode."""
        return 0

    def am_rel(self) -> int:
        """Relative addressing mode."""
        return 0

    def am_abs(self) -> int:
        """Absolute addressing mode."""
        return 0

    def am_abx(self) -> int:
        """Absolute addressing X mode."""
        return 0

    def am_aby(self) -> int:
        """Absolute addressing Y mode."""
        return 0

    def am_ind(self) -> int:
        """Indirect addressing mode."""
        return 0

    def am_izx(self) -> int:
        """Indirect X addressing mode."""
        return 0

    def am_izy(self) -> int:
        """Indirect Y addressing mode."""
        return 0

    # opcodes
    def op_adc(self) -> int:
        """Opcode ADC"""
        return 0

    def op_and(self) -> int:
        """Opcode AND"""
        return 0

    def op_asl(self) -> int:
        """Opcode ASL"""
        return 0

    def op_bcc(self) -> int:
        """Opcode BCC"""
        return 0

    def op_bcs(self) -> int:
        """Opcode BCS"""
        return 0

    def op_beq(self) -> int:
        """Opcode BEQ"""
        return 0

    def op_bit(self) -> int:
        """Opcode BIT"""
        return 0

    def op_bmi(self) -> int:
        """Opcode BMI"""
        return 0

    def op_bne(self) -> int:
        """Opcode BNE"""
        return 0

    def op_bpl(self) -> int:
        """Opcode BPL"""
        return 0

    def op_brk(self) -> int:
        """Opcode BRK"""
        return 0

    def op_bvc(self) -> int:
        """Opcode BVC"""
        return 0

    def op_bvs(self) -> int:
        """Opcode BVS"""
        return 0

    def op_clc(self) -> int:
        """Opcode CLC"""
        return 0

    def op_cld(self) -> int:
        """Opcode CLD"""
        return 0

    def op_cli(self) -> int:
        """Opcode CLI"""
        return 0

    def op_clv(self) -> int:
        """Opcode CLV"""
        return 0

    def op_cmp(self) -> int:
        """Opcode CMP"""
        return 0

    def op_cpx(self) -> int:
        """Opcode CPX"""
        return 0

    def op_cpy(self) -> int:
        """Opcode CPY"""
        return 0

    def op_dec(self) -> int:
        """Opcode DEC"""
        return 0

    def op_dex(self) -> int:
        """Opcode DEX"""
        return 0

    def op_dey(self) -> int:
        """Opcode DEY"""
        return 0

    def op_eor(self) -> int:
        """Opcode EOR"""
        return 0

    def op_inc(self) -> int:
        """Opcode INC"""
        return 0

    def op_inx(self) -> int:
        """Opcode INX"""
        return 0

    def op_iny(self) -> int:
        """Opcode INY"""
        return 0

    def op_jmp(self) -> int:
        """Opcode JMP"""
        return 0

    def op_jsr(self) -> int:
        """Opcode JSR"""
        return 0

    def op_lda(self) -> int:
        """Opcode LDA"""
        return 0

    def op_ldx(self) -> int:
        """Opcode LDX"""
        return 0

    def op_ldy(self) -> int:
        """Opcode LDY"""
        return 0

    def op_lsr(self) -> int:
        """Opcode LSR"""
        return 0

    def op_nop(self) -> int:
        """Opcode NOP"""
        return 0

    def op_ora(self) -> int:
        """Opcode ORA"""
        return 0

    def op_pha(self) -> int:
        """Opcode PHA"""
        return 0

    def op_php(self) -> int:
        """Opcode PHP"""
        return 0

    def op_pla(self) -> int:
        """Opcode PLA"""
        return 0

    def op_plp(self) -> int:
        """Opcode PLP"""
        return 0

    def op_rol(self) -> int:
        """Opcode ROL"""
        return 0

    def op_ror(self) -> int:
        """Opcode ROR"""
        return 0

    def op_rti(self) -> int:
        """Opcode RTI"""
        return 0

    def op_rts(self) -> int:
        """Opcode RTS"""
        return 0

    def op_sbc(self) -> int:
        """Opcode SBC"""
        return 0

    def op_sec(self) -> int:
        """Opcode SEC"""
        return 0

    def op_sed(self) -> int:
        """Opcode SED"""
        return 0

    def op_sei(self) -> int:
        """Opcode SEI"""
        return 0

    def op_sta(self) -> int:
        """Opcode STA"""
        return 0

    def op_stx(self) -> int:
        """Opcode STX"""
        return 0

    def op_sty(self) -> int:
        """Opcode STY"""
        return 0

    def op_tax(self) -> int:
        """Opcode TAX"""
        return 0

    def op_tay(self) -> int:
        """Opcode TAY"""
        return 0

    def op_tsx(self) -> int:
        """Opcode TSX"""
        return 0

    def op_txa(self) -> int:
        """Opcode TXA"""
        return 0

    def op_txs(self) -> int:
        """Opcode TXS"""
        return 0

    def op_tya(self) -> int:
        """Opcode TYA"""
        return 0

    def op_xxx(self) -> int:
        """Illegal opcode"""
        return -1
