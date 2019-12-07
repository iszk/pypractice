#!/bin/env python

def add(n, m):
    return n + m

def wrapper(func, n, m):
    return func(n, m)

def wrapper_optinal(func, *args):
    return func(*args)

if __name__ == '__main__':
    print("直接実行")
    v1 = add(2, 3)
    print("add(n, m) = {}".format(v1))

    print("----")

    print("wrapper")
    v2 = wrapper(add, 2, 3)
    print("wrapper(add, n, m) = {}".format(v2))

    print("----")

    print("wrapper可変長引数")
    v3 = wrapper_optinal(add, 2, 3)
    print("wrapper_optional(add, n, m) = {}".format(v3))


