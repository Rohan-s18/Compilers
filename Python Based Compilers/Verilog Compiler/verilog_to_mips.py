

def verilog_to_mips(verilog_instruction):
    if verilog_instruction.startswith('add'):
        # Split the instruction into its operands
        operands = verilog_instruction.split(' ')[1:]
        
        # Map the Verilog registers to their MIPS equivalents
        mips_registers = {
            'r1': '$s1',
            'r2': '$s2',
            'r3': '$s3'
        }
        
        # Build the MIPS instruction string with the mapped registers
        #mips_instruction = f"add {mips_registers[operands[0]]}, {mips_registers[operands[1]]}, {mips_registers[operands[2]]}"
        mips_instruction = "add {}, {}, {}".format(mips_registers[operands[0]], mips_registers[operands[1]], mips_registers[operands[2]])


        return mips_instruction
    else:
        raise ValueError("Unsupported Verilog instruction")
    
def verilog_if_to_mips(verilog_if_statement):
    if verilog_if_statement.startswith('if'):
        # Split the if statement into its condition and body
        condition, body = verilog_if_statement.split(') ')

        # Strip the parentheses from the condition
        condition = condition.split('(')[1]

        # Convert the condition to MIPS branch instruction
        mips_condition = condition.replace('==', 'beq').replace('!=', 'bne').replace('>', 'bgt').replace('<', 'blt')

        # Map the Verilog registers to their MIPS equivalents
        mips_registers = {
            'r1': '$s1',
            'r2': '$s2',
            'r3': '$s3'
        }

        # Replace Verilog registers with their MIPS equivalents in the body
        for verilog_reg, mips_reg in mips_registers.items():
            body = body.replace(verilog_reg, mips_reg)

        # Construct the MIPS if statement
        mips_if_statement = "{mips_condition} {body}"
        
        return mips_if_statement
    else:
        raise ValueError("Unsupported Verilog if statement")
    

#Main function for testing
def main():
    verilog_instruction = "add r1, r2, r3"
    mips_instruction = verilog_to_mips(verilog_instruction)
    print(mips_instruction)

    verilog_if_statement = "if (r1 == r2) r3 = r1 + r2;"
    lmao = verilog_if_to_mips(verilog_if_statement)
    print(lmao)

if __name__ == "__main__":
    main()
