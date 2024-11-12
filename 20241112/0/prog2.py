class A:
    __v=0
    def inc(self):
        self.__v+=1
        print(self.__v)
class B(A):
    v=100500