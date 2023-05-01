"""
Author: Rohan Singh
Driver For the Verilog -> MIPS Compiler
"""


#  Importing the parsing + emitting functions for the various types of verilog statements
import verilog_loops as vl
import verilog_to_mips as vm
import additional_verilog as av
import verilog_header as vh



#  Driver function for the compiler
def compile(file_in, file_out):
    

    # Initial check to see if the header format is correct
    try:
        with open(file_in, 'r') as file:
            data = file.read().replace('\n', ' ')
        
        vh.parse_verilog_module_header(data)
        print("Verilog file has correct header")

    except Exception as e:
        print("Compiler Error: Incorrect File Header")
        return
    
    # opening the file
    file_obj = open(file_in, "r")
  
    # reading the data from the file
    file_data = file_obj.read()
  
    # splitting the file data into lines
    lines = file_data.splitlines()
    #print(lines)
    file_obj.close()

    #This list will contain the compiled mips instructions
    out = []

    #Fetching the translated instructions
    for line in lines:
        instr = choose(line)
        for i in instr:
            out.append(i)

    fout = open(file_out,"w")

    #Writing the instructions
    for o in out:
        fout.write(o)
        fout.write("\n")
    
    
    return out



#  Function to choose the function
def choose(instruction):
    out = []

    #Selecting the instruction
    if(instruction.startswith("add")):
        out.append(vm.vadd(instruction))
    elif(instruction.startswith("if")):
        out.append(vm.vif(instruction))
    elif(instruction.startswith("for")):
        temp = vl.verilog_loop_to_mips(instruction)
        for tempu in temp:
            out.append(tempu)
    #else:
        #out = av.convert_assign_to_mips(instruction)

    return out

    


#  Main function for testing purposes
def main():
    

    source = "/Users/rohansingh/github_repos/Compilers/Python Based Compilers/Verilog Compiler/Verilog/verilog_code.sv"
    dest = "/Users/rohansingh/github_repos/Compilers/Python Based Compilers/Verilog Compiler/MIPS/mips_code.asm"

    #Calling the compiler driver
    result = compile(source,dest)

    print(result)


if __name__ == "__main__":
    main()

