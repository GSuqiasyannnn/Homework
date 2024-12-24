##                                HOMEWORK

# import math
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def t_sides(self):
#         if self.a + self.b < self.c:
#             raise Exception('The sides is not True')
#         elif self.a + self.c < self.b:
#             raise Exception('The sides is not True')
#         elif self.c + self.b < self.a:
#             raise Exception('The sides is not True')
#         return
#
#     def k(self, k_sin):
#         k_sin = self.a / math.sin(self.a) == self.b / math.sin(self.b) == self.c == math.sin(self.c)
#         return f'{k_sin}'
#
#     def p(self):
#         p = self.a + self.b + self.b
#         print(f'{p}')
#
#     def s(self, p, s):
#         p = (self.a + self.b + self.c) / 2
#         s = p * (p - self.a) * (p - self.b) * (p - self.c) ** 0.5
#         return s
#
#     def t_equilateral(self):
#         if self.a == self.c == self.b:
#             return 'The Triangle is equilateral. '
#         elif self.a != self.b != self.c :
#             return "The Triangle is not equilateral"
#
#     def isosceles(self):
#         if self.a / math.sin(self.a) == self.b / math.sin(self.b) != self.c / math.sin(self.c):
#             return 'The triangle is isosceles'
#
#     def scalene(self):
#         if self.a / math.sin(self.a) != self.b / math.sin(self.b) != self.c / math.sin(self.c):
#           return 'The triangle is scalene '
#
#     def right(self):
#         if (self.c ** 2 ) == (self.a ** 2 ) + (self.b ** 2):
#             return 'The triangle is right'
#         elif (self.c ** 2) != (self.a ** 2) + (self.b ** 2):
#             return 'The triangle is  not right'
#