from functools import wraps


class Fix:
    def __init__(self, n):
        self.n = n

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            new_args = []
            for i in range(len(args)):
                if isinstance(args[i], float):
                    new_args.append(round(args[i], self.n))
                else:
                    new_args.append(args[i])
            new_kwargs = {}
            for i in kwargs.keys():
                if isinstance(kwargs[i], float):
                    new_kwargs[i] = round(kwargs[i], self.n)
                else:
                    new_kwargs[i] = kwargs[i]
            result = f(*new_args, **new_kwargs)
            return round(result, self.n) if isinstance(result, float) else result

        return wrapper

