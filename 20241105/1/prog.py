class Omnibus:
    _attr_counts = {}

    def __init__(self):
        object.__setattr__(self, '_attributes_set', set())

    def __setattr__(self, name, value):
        if name.startswith('_'):
            setattr(self, name, value)
        else:
            if name not in self._attributes_set:
                self._attributes_set.add(name)
                Omnibus._attr_counts[name] = Omnibus._attr_counts.get(name, 0) + 1

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        return Omnibus._attr_counts.get(name, 0)

    def __delattr__(self, name):
        if name.startswith('_'):
            delattr(self, name)
        else:
            if name in self._attributes_set:
                self._attributes_set.remove(name)
                if Omnibus._attr_counts.get(name, 0) > 0:
                    Omnibus._attr_counts[name] -= 1
                    if Omnibus._attr_counts[name] == 0:
                        del Omnibus._attr_counts[name]

    def __str__(self):
        return f"Omnibus(set={self._attributes_set})"

while s:=input():
    exec(s)


