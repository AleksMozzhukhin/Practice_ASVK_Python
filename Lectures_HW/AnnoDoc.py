class AnnoDoc(type):
    def __new__(metacls, name, bases, namespace):
        cls = super().__new__(metacls, name, bases, namespace)
        annotations = getattr(cls, '__annotations__', {}).copy()
        doc_lines = []
        if cls.__doc__:
            doc_lines.append(cls.__doc__)
        for attr, annot in annotations.items():
            if isinstance(annot, str):
                doc_lines.append(f"{attr}: {annot}")
                if attr in cls.__dict__:
                    value = getattr(cls, attr)
                    cls.__annotations__[attr] = type(value)
                else:
                    del cls.__annotations__[attr]

        if doc_lines:
            cls.__doc__ = "\n".join(doc_lines)

        return cls