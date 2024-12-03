class Sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError('only one parent allowed')
        return super().__new__(metacls, name, parents, namespace)