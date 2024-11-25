class SizeDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if hasattr(instance, '_size') and instance._size is not None:
            return instance._size
        if hasattr(instance, '__len__'):
            return len(instance)
        if hasattr(instance, '__abs__'):
            return abs(instance)
        return 0

    def __set__(self, instance, value):
        instance._size = value

    def __delete__(self, instance):
        instance._size = None


def sizer(cls):
    cls.size = SizeDescriptor()
    return cls

