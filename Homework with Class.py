class MyList:
    def __init__(self, *args):
        self._l = list(args)

    def add(self, obj):
        self._l.append(obj)

    def prod(self):
        p = 1
        for i in self._l:
            p *= i
        return p

    def counter(self):
        return self._l.count


    def pop(self):
        for i in self._l:
           return self._l.pop(i[-4])


    def clear(self):
        return self._l.clear()

    def copy(self):
        return self._l.copy()

    def extend(self, lst):
           return self._l.extend(lst)
    
    def index(self, lst):
        lst = [1, 2, 3, 4, 5, 6, 7, 4, 3, 2]
        return self._l.index(lst, 2, 6)

    def reverse(self):
        return self._l.reverse()

    def sort(self):
        return self._l.sort()


