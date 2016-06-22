print '---------------------------------1--------------------------------'


class Collection(object):
    iterator = []

    def get(self, i):
        pass

    def size(self):
        pass


class Iterator(object):
    def previous(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass

    def first(self):
        pass


class MyCollection(Collection):

    strings = ["A", "B", "C", "D", "E"]

    def iterator(self):
        return MyIterator(self)

    def get(self, i):
        return self.strings[i]

    def size(self):
        return len(self.strings)


class MyIterator(Iterator):

    collection = None
    pos = -1

    def __init__(self, collection):
        self.collection = collection

    def previous(self):
        if self.pos > 0:
            self.pos -= 1
        return self.collection.get(self.pos)

    def next(self):
        if self.pos < (self.collection.size() - 1):
            self.pos += 1
        return self.collection.get(self.pos)

    def hasNext(self):
        if self.pos < (self.collection.size() - 1):
            return True
        else:
            return False

    def first(self):
        return self.collection.get(0)


def Test():
    collection = MyCollection()
    it = collection.iterator()
    while it.hasNext():
        print it.next()
Test()


print '---------------------------------2--------------------------------'
# http://stackoverflow.com/questions/9884132/what-exactly-are-pythons-
# iterator-iterable-and-iteration-protocols

"""
Iteration is a general term for taking each item of something,
one after another. Any time you use a loop, explicit or implicit,
to go over a group of items, that is iteration.

In Python, iterable and iterator have specific meanings.

An iterable is an object that has an __iter__ method which returns an iterator,
or which defines a __getitem__ method that can take sequential indexes starting
from zero (and raises an IndexError when the indexes are no longer valid).
So an iterable is an object that you can get an iterator from.

An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

Whenever you use a for loop, or map, or a list comprehension, etc. in Python,
the next method is called automatically to get each item from the iterator,
thus going through the process of iteration.
"""


print type(list)


class MyIterator2(object):
    _data = []
    pos = 0

    def __init__(self):
        self._data = []
        self.pos = 0

    def __iter__(self):
        return self

    def __getitem__(self, index):
        if len(self._data) == 0 or index > len(self._data) or index < 0:
            raise IndexError
        return self._data[index]

    def append(self, data):
        self._data.append(data)

    def next(self):
        try:
            data = self._data[self.pos]
            self.pos += 1
            return data
        except IndexError:
            raise StopIteration

    def __next__(self):
        return self.next()

a = MyIterator2()

a.append(1)
a.append(2)

print a[0]
print a[1]

for item in a:
    print item

try:
    print a[2]
except IndexError:
    print "out of range, 2"

b = MyIterator2()

try:
    print b[0]
except IndexError:
    print "out of range, 0"

try:
    print b[-1]
except IndexError:
    print "out of range, -1"
