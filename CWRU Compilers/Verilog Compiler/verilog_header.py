"""
Author: Rohan Singh
Parser for verilog file headers
"""


def parse_verilog_module_header(verilog_code):
    # Find the module declaration
    module_declaration_start = verilog_code.find('module')
    if module_declaration_start == -1:
        raise ValueError("No module declaration found")

    # Find the module name
    module_name_start = module_declaration_start + len('module')
    module_name_end = verilog_code.find('(', module_name_start)
    if module_name_end == -1:
        raise ValueError("Invalid module declaration")
    module_name = verilog_code[module_name_start:module_name_end].strip()

    # Find the module ports
    port_list_start = module_name_end + 1
    port_list_end = verilog_code.find(');', port_list_start)
    if port_list_end == -1:
        raise ValueError("Invalid module declaration")
    port_list = verilog_code[port_list_start:port_list_end].split(',')
    ports = [port.strip() for port in port_list]


    # Return a dictionary containing the module name and its ports
    return {
        'name': module_name,
        'ports': ports
    }


#Main function for testing
def main():
    verilog_code = """
module my_module(input a, input b, output c, output d);
    add r1, r2, r3
    rkfnrlgm
    rkngtlg
    ktnotm
endmodule
"""

    module_info = parse_verilog_module_header(verilog_code)
    print(module_info)


if __name__ == "__main__":
    main()
