from collections import UserList


class Ulist(UserList):
    def __init__(self, info=[]):
        UserList.__init__(self)
        self.info = info

    def add_iterable(self, iterable):
        for i in iterable:
            if i in self:
                print("%r This is already in the list." % (i))
            else:
                UserList.append(self, i)
        return self

    def __add__(self, something_new):
        if hasattr(something_new, "__iter__"):
            return self.add_iterable(something_new)
        else:
            return UserList.append(self, something_new)

    def append(self, something_new):
        if something_new in self:
            print("%r This is already in the list." % (something_new))
        else:
            return UserList.append(self, something_new)

    def extend(self, something_new):
        return self.add_iterable(something_new)
