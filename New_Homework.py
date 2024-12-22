## ex 1
import math
def function(r, alpha ):
    s = (math.pi * r ** 2 ) * alpha / 360
    return s

print(function(r= 10, alpha=23))

## ex 3
def filter_(words):
        result = []
        max_len = max(len(i) for i in words)
        for i in words:
           if len(i) == max_len:
               result.append(i)
        return result
print(filter_(words=["aba", "aa", "z", "ad", "vcd", "aba"]))