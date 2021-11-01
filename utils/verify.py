# class A:
#     a = 1
#
#     def test1(self):
#         self.test11 = "test1"
#         print(self.test11)
#         return self
#
#     def test2(self):
#         self.test22 = "test2"
#         print(self.test22)
#
#
# A.b = 2
#
# obj = A()
# obj.c = 3
# print(id(A))
# print(id(obj))
# t = obj.test1().__class__
# print(id(t))
# print(A.b)
# print(obj.c)

# class A:
#     def __init__(self, a, b):
#         print(a, b)    #4
#
#
# class B(A):
#     def __init__(self, a, b, c):   #最开始执行1
#         print(0)                    # 2
#         A.__init__(self, a=a, b=b) # 然后执行 3
#         print(c)    # 5
#
#
# b = B(1,2,3)


class Base:
    a = 1

    def __init__(self):
        self.ab = 12
        print(self.ab)

    def test(self):
        print(self.a)


class B(Base):
    b = 2

    def __init__(self):
        self.cd = 34
        print(self.cd)

    def test_b(self):
        print(self.b)


obj = B()


class C(Base):
    c = 3

    def test_c(self):
        print(self.c)


class D(B, C):
    d = 4

    def test_d(self):
        print(self.d)

#
# print(obj.test(), obj.test_b(), obj.test_d(),'--------')
#
# obj1 = B()
# print(obj1.test(),obj1.test_b())


# class  A1:
#     test_class = 1
#
#     def test_01(self):
#         print(self.test_class)
#
#
#
# A1().test_01()
