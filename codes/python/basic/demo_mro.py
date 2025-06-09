class X:
    pass


class Y:
    pass


class A(X, Y):
    pass


class B(Y, X):
    pass


class Z(A, B):
    pass  # TypeError: Cannot create consistent method resolution order (MRO)


def main():
    pass


if __name__ == '__main__':
    main()

"""
Traceback (most recent call last):
  File "/Users/huoyinghui/github/hello-algo/codes/python/basic/demo_mro.py", line 17, in <module>
    class Z(A, B):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases X, Y
"""