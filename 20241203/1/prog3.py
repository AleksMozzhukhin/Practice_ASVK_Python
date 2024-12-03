class Doubleton:
    _instance = None
    _count = 0

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance.append(super().__call__(*args, **kw))
        cls._count += 1
        return cls._instance
