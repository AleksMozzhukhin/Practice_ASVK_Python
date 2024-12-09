class dump(type):
    def __new__(metacls, name, bases, namespace):
        def wrap_method(method, method_name):
            def wrapped(self, *args, **kwargs):
                print(f"{method_name}: {args}, {kwargs}")
                return method(self, *args, **kwargs)
            return wrapped

        for attr_name, attr_value in namespace.items():
            if callable(attr_value):
                namespace[attr_name] = wrap_method(attr_value, attr_name)

        return super().__new__(metacls, name, bases, namespace)


import sys
program_input = sys.stdin.read()
exec(program_input)
