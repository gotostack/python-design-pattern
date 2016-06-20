import copy


class Cloneable(object):
    def clone(self):
        return copy.copy(self)

    def deepclone(self):
        return copy.deepcopy(self)


class Prototype(Cloneable):

    def clone(self):
        proto = super(Prototype, self).clone()
        return proto

    def deepclone(self):
        proto = super(Prototype, self).deepclone()
        return proto


class PersonA(Prototype):
    name = ''

    def __init__(self, name):
        self.name = name


a = PersonA("zhangsan")
print a.name
a.name = 'lisi'
print a.name


print id(a)


b = a.clone()
print b.name
print id(b)
b.name = 'wanwu'
print b.name


b = a.deepclone()
print b.name
print id(b)
b.name = 'wanwu'
print b.name
