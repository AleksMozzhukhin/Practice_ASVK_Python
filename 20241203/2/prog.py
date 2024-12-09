import sys
import math

def interpret_program(program_lines):
    program = [line.strip() for line in program_lines]
    commands = []
    labels = {}
    for idx, line in enumerate(program):
        if not line:
            continue
        parts = line.split()

        if parts[0].endswith(':'):
            label = parts[0][:-1]
            if label in labels:
                pass
            labels[label] = len(commands)
            parts = parts[1:]

        if not parts:
            continue

        command = parts
        commands.append(command)
    jump_commands = {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'}

    for command in commands:
        if not command:
            continue
        op = command[0]
        if op in jump_commands:
            if len(command) != 4:
                continue
            label = command[3]
            if label not in labels:
                return
    variables = {}
    def get_value(param):
        try:
            return float(param)
        except ValueError:
            return variables.get(param, 0.0)

    def execute_operation(op, src, operand, dest):
        a = get_value(src)
        b = get_value(operand)
        try:
            if op == 'add':
                result = a + b
            elif op == 'sub':
                result = a - b
            elif op == 'mul':
                result = a * b
            elif op == 'div':
                if b == 0:
                    result = math.inf
                else:
                    result = a / b
            else:
                result = 0.0
        except:
            result = math.inf
        variables[dest] = result
    def execute_comparison(op, src, operand, label):
        a = get_value(src)
        b = get_value(operand)
        condition = False
        if op == 'ifeq':
            condition = a == b
        elif op == 'ifne':
            condition = a != b
        elif op == 'ifgt':
            condition = a > b
        elif op == 'ifge':
            condition = a >= b
        elif op == 'iflt':
            condition = a < b
        elif op == 'ifle':
            condition = a <= b
        if condition:
            return labels[label]
        return None
    pc = 0
    output = []
    while pc < len(commands):
        command = commands[pc]
        if not command:
            pc +=1
            continue
        op = command[0]
        if op == 'stop':
            break

        elif op == 'store':
            if len(command) != 3:
                pc +=1
                continue
            number, dest = command[1], command[2]
            try:
                value = float(number)
            except ValueError:
                value = 0.0
            variables[dest] = value

        elif op in {'add', 'sub', 'mul', 'div'}:
            if len(command) != 4:
                pc +=1
                continue
            src, operand, dest = command[1], command[2], command[3]
            execute_operation(op, src, operand, dest)

        elif op in {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'}:
            if len(command) != 4:
                pc +=1
                continue
            src, operand, label = command[1], command[2], command[3]
            new_pc = execute_comparison(op, src, operand, label)
            if new_pc is not None:
                pc = new_pc
                continue
        elif op == 'out':
            if len(command) !=2:
                pc +=1
                continue
            src = command[1]
            value = get_value(src)
            output.append(value)
        else:
            pass

        pc +=1
    for val in output:
        print(val)

import sys
program_input = sys.stdin.read().splitlines()
interpret_program(program_input)
