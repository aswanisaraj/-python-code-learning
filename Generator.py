"""In Python, a generator is a special type of iterator that allows for lazy evaluation of data. It's defined using
the yield keyword, which temporarily suspends the execution of the function and returns a value to the caller. When
the generator function is called again, it resumes execution from where it left off, and continues generating the
sequence of values until it reaches the end. Generators are useful for working with large sequences of data without
having to load everything into memory at once.

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)

h = "Jehangeer"
iter = iter(h)
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())





