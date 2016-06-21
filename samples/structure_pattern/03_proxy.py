print '---------------------------------1--------------------------------'


class Interface(object):

    def Request(self):
        return 0


class RealSubject(Interface):

    def Request(self):
        print "Real request."


class Proxy(Interface):

    def Request(self):
        self.real = RealSubject()
        self.real.Request()


def test1():
    p = Proxy()
    p.Request()
test1()


print '---------------------------------2--------------------------------'


class Sourceable(object):
    def method(self):
        pass


class Source(Sourceable):
    def method(self):
        print "the original method!"


class Proxy2(Sourceable):
    source = None

    def __init__(self):
        # super()
        self.source = Source()

    def method(self):
        self.before()
        self.source.method()
        self.atfer()

    def atfer(self):
        print "after proxy!"

    def before(self):
        print "before proxy!"


def test2():
    source = Proxy2()
    source.method()
test2()
