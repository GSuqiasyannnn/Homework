class Calculator:
    def __init__(self, num):
        if isinstance(num, int | float):
            self._num = num
            print('The number is int | float')
        else:
            raise Exception('Invalid parameter')

    @property
    def number(self):
        return self._num

    def __add__(self, other):
        return Calculator(self._num + other.number)

    def __sub__(self, other):
        return Calculator(self._num - other.number)

    def __mul__(self, other):
        return Calculator(self._num * other.number)

    def __truediv__(self, other):
        return Calculator(self._num / other.number)

    def __floordiv__(self, other):
        return Calculator(self._num // other.number)

    def __mod__(self, other):
        return Calculator(self._num % other.number)

    def __pow__(self, other):
        return Calculator(self._num ** other.number)

    def __iadd__(self, other):
        if isinstance(other, Calculator):
            self._num += other.number
        else:
            self._num += other
        return self

    def __isub__(self, other):
        if isinstance(other, Calculator):
            self._num -= other.number
        else:
            self._num -= other.number
        return self

    def __imul__(self, other):
        if isinstance(other, Calculator):
            self._num *= other.number
        else:
            self._num *= other.number
        return self

    def __itruediv__(self, other):
        if isinstance(other, Calculator):
            self._num /= other.number
        else:
            self._num /= other.number
        return self

    def __rfloordiv__(self, other):
        if isinstance(other, Calculator):
            self._num //= other.number
        else:
            self._num //= other.number
        return self

    def __imod__(self, other):
        if isinstance(other, Calculator):
            self._num %= other.number
        else:
            self._num %= other.number
        return self

    def __ipow__(self, other):
        if isinstance(other, Calculator):
            self._num **= other.number
        else:
            self._num **= other.number
        return self


    def __eq__(self, other):
        return Calculator(self._num == other.number)

    def __ne__(self, other):
        return Calculator(self._num != other.number)

    def __lt__(self, other):
        return Calculator(self._num < other.number)

    def __le__(self, other):
        return Calculator(self._num <= other.number)

    def __gt__(self, other):
        return Calculator(self._num > other.number)

    def __ge__(self, other):
        return Calculator(self._num >= other.number)

