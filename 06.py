#!/usr/bin/python

def foo(bar=None):
    if bar==None:
        bar = []
    bar.append('o')
    return bar

#! fix the function so all calls return the same
print(foo())
print(foo())
print(foo())
print(foo([]))
