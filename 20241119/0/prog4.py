class Sender:
    first_use = True

    @classmethod
    def report(cls):
        if cls.first_use:
            print("Greetings!")
            cls.first_use = False
        else:
            print("Get away!")


class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            i.report()


a = [Sender(), Sender(), Sender()]

Asker.askall(a)
