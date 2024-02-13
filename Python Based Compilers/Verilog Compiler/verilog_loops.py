"""
Author: Rohan Singh
Parser for verilog loops
"""

#Function to parse verilog loops
def verilog_loop_to_mips(verilog_loop):
    # Split the Verilog loop into its components
    loop_components = verilog_loop.split(' ')
    loop_components = list(filter(None, loop_components))  # Remove empty strings from list

    # Determine the loop label and bounds
    loop_label = loop_components[1]
    loop_label = "loop_label"
    loop_start = loop_components[3]
    loop_end = loop_components[6]

    # Determine the register to use for the loop index
    index_register = '$s0'

    # Generate the MIPS instructions for the loop
    mips_instructions = []
    mips_instructions.append("li {0}, {1}".format(index_register, loop_start))  # Initialize loop index
    mips_instructions.append("{0}:".format(loop_label))  # Loop label
    mips_instructions.append("bge {0}, {1}, exit_loop".format(index_register, loop_end))  # Branch if index >= end
    # Loop body instructions go here
    mips_instructions.append("addi {0}, {0}, 1".format(index_register))  # Increment loop index
    mips_instructions.append("j {0}".format(loop_label))  # Jump back to loop label
    mips_instructions.append("exit_loop:")

    return mips_instructions


def main():
    verilog_loop = "for (i = 0; i < 10; i = i + 1) begin"
    mips_instructions = verilog_loop_to_mips(verilog_loop)
    #print('\n'.join(mips_instructions))

if __name__ == "__main__":
    main()
