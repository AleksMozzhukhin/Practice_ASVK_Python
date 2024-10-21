from math import *

def parse_constant(string):
    string = string.strip()
    if (string.startswith('"') and string.endswith('"')) or (string.startswith("'") and string.endswith("'")):
        return string[1:-1]
    else:
        try:
            return int(string)
        except ValueError:
            try:
                return float(string)
            except ValueError:
                return string


functions = {'quit': {
    'params': ['s'],
    'expression': 's.format(num_functions, num_lines)'
}}
string_count = 0
while s := input():
    string_count += 1
    if s[0] == ':':
        tmp = s[1:].split()
        functions[tmp[0]] = {
            "params": tmp[1:-1],
            "expression": tmp[-1]
        }
    else:
        tmp = s.split()
        if len(functions[tmp[0]]["params"]) == 0:
            args = []
        elif len(functions[tmp[0]]["params"]) == 1:
            arg = s[len(tmp[0]):].strip()
            args = [arg]
        else:
            args = tmp[1:]
        local_vars = {}
        for name, value in zip(functions[tmp[0]]["params"], args):
            local_vars[name] = parse_constant(value)

        if tmp[0] == 'quit':
            local_vars['num_functions'] = len(functions.keys())
            local_vars['num_lines'] = string_count

        result = eval(functions[tmp[0]]["expression"], None, local_vars)
        print(result)

        if tmp[0] == 'quit':
            break
