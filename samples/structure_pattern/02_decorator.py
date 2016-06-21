print '---------------------------------1--------------------------------'


class Person:
    def __init__(self, tname):
        self.name = tname

    def Show(self):
        print "dressed %s" % (self.name)


class Finery(Person):
    componet = None

    def __init__(self):
        pass

    def Decorate(self, ct):
        self.componet = ct

    def Show(self):
        if self.componet:
            self.componet.Show()


class TShirts(Finery):
    def __init__(self):
        pass

    def Show(self):
        print "Big T-shirt "
        self.componet.Show()


class BigTrouser(Finery):
    def __init__(self):
        pass

    def Show(self):
        print "Big Trouser "
        self.componet.Show()


def test1():
    p = Person("somebody")
    bt = BigTrouser()
    ts = TShirts()
    bt.Decorate(p)
    ts.Decorate(bt)
    ts.Show()

test1()


print '---------------------------------2--------------------------------'


class Sourceable(object):
    def method(self):
        pass


class Source(Sourceable):
    def method(self):
        print "the original method!"


class Decorator(Sourceable):
    source = None

    def __init__(self, source):
        # super()
        self.source = source

    def method(self):
        print "before decorator!"
        self.source.method()
        print "after decorator!"


def test2():
    source = Source()
    obj = Decorator(source)
    obj.method()
test2()


print '---------------------------------python decorator-------------------'


def wap1(func):
    def _wap():
        print "before 1"
        func()
        print "end 1"
    return _wap


def wap2(func):
    def _wap():
        print "before 2"
        func()
        print "end 2"
    return _wap


@wap1
@wap2
def method():
    print "I will do something"


method()
