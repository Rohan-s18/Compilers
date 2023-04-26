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
    print(lines)
    file_obj.close()
    
    out = ""
    



    



#  Main function for testing purposes
def main():
    
    #Calling the compiler driver
    compile("/Users/rohansingh/github_repos/Compilers/Python Based Compilers/Verilog Compiler/verilog_header.txt","")


if __name__ == "__main__":
    main()

