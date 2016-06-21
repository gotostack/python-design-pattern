class Target(object):
    def Request(self):
        print "common request."


class Adaptee(Target):
    def SpecificRequest(self):
        print "specific request."


class Adapter(Target):
    def __init__(self, ada):
        self.adaptee = ada

    def Request(self):
        self.adaptee.SpecificRequest()


adaptee = Adaptee()
adapter = Adapter(adaptee)
adapter.Request()


print '----------------------------------2-------------------------'


class Source(object):
    def method1(self):
        print "this is original method!"


class Targetable(object):
    def method1(self):
        pass

    def method2(self):
        pass


class Adapter2(Source, Targetable):
    def method2(self):
        print "this is the targetable method!"

target = Adapter2()
target.method1()
target.method2()


print '----------------------------------3--------------------------'


class Wrapper(Targetable):
    source = None

    def __init__(self, source):
        # super();
        self.source = source

    def method2(self):
        print "this is the targetable method!"

    def method1(self):
        self.source.method1()

source = Source()
target = Wrapper(source)
target.method1()
target.method2()


print '--------------------------------4-------------------------'


class Sourceable(object):
    def method1(self):
        pass

    def method2(self):
        pass


class Wrapper2(Sourceable):
    def method1(self):
        pass

    def method2(self):
        pass


class SourceSub1(Wrapper2):
    def method1(self):
        print "the sourceable interface's first Sub1!"


class SourceSub2(Wrapper2):
    def method1(self):
        print "the sourceable interface's second Sub2!"


source1 = SourceSub1()
source2 = SourceSub2()

source1.method1()
source1.method2()
source2.method1()
source2.method2()
