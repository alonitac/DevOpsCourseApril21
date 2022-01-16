def foo(p1, p2, p3):
    pass


def boo(p1, *args, k1=1, hi='bye', **kwargs):
    pass


foo(1, 2, 3)  # good
# foo(1, 2)     # bad


boo(1, 2, 3, k1=2, ignore=True)
print(1, '555', 3)
print(1, 2, None, 6, 6, 7, 8, 7, 6)
print()





