def convert_assign_to_mips(verilog_assign_statement):
    # Split the assign statement into its LHS and RHS expressions
    lhs, rhs = verilog_assign_statement.split('=')
    lhs = lhs.strip()
    rhs = rhs.strip()

    # Determine the register to store the RHS value in
    # For simplicity, let's assume that the LHS is a register name (e.g. r1)
    register = "$s{}".format(lhs[1:])

    # Generate the MIPS instruction to store the RHS value in the specified register
    mips_instruction = "li {}, {}".format(register, rhs)

    return mips_instruction


def main():
    instr =  "r1 = r2 + r3;"
    pass

if __name__ == "__main__":
    main()