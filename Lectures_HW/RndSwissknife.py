import random
from collections.abc import Sequence, Iterable


def rnd(a, b=None):
    match (a, b):
        case (int(), None):
            return random.randint(0, a)

        case (int(), int()):
            return random.randint(a, b)

        case (float(), (int() | float())):
            return random.uniform(a, b)

        case (str(), str()):
            return random.choice(a.split(b))

        case (str(), int()):
            start = random.randint(0, len(a) - b)
            return a[start:start + b]

        case (str(), None):
            return random.choice(a.split())

        case (Iterable() | Sequence(), None):
            return random.choice(list(a))

        case (Iterable() | Sequence(), int()):
            return random.choices(list(a), k=b)
