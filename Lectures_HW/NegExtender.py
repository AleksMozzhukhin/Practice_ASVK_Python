class NegExt:
    def __neg__(self):
        my_mro=self.__class__.mro()
        parent=my_mro[my_mro.index(NegExt)+1]
        try:
            return self.__class__(parent.__neg__(self))
        except Exception:
            try:
                return self.__class__(self[1:-1])
            except Exception:
                return self.__class__(self)