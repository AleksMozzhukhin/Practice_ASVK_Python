my_globals = {"__builtins__": {}}
my_locals = {}
while s := input():
    s = s.strip()
    if s[0] == '#':
        continue
    if "=" in s:
        left, right = map(str.strip, s.split('=', 1))

        if not left.isidentifier():
            print("Assignment error")
            continue
        try:
            my_locals[left] = eval(right, my_globals, my_locals)
        except NameError:
            print("Name error")
        except SyntaxError:
            print("Syntax error")
        except Exception:
            print("Runtime error")
        continue
    try:
        results = eval(s, my_globals, my_locals)
        print(results)
    except NameError:
        print("Name error")
    except SyntaxError:
        print("Syntax error")
    except Exception:
        print("Runtime error")
