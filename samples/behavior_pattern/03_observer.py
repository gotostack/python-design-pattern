print '---------------------------------1--------------------------------'


class Observer:
    def __init__(self, strname, strsub):
        self.name = strname
        self.sub = strsub

    def Update(self):
        pass


class StockObserver(Observer):
    def Update(self):
        print "%s:%s, stop watching Stock and go on work!" % (self.name,
                                                              self.sub.action)


class NBAObserver(Observer):
    def Update(self):
        print "%s:%s, stop watching NBA and go on work!" % (self.name,
                                                            self.sub.action)


class SecretaryBase:
    def __init__(self):
        self.observers = []

    def Attach(self, new_observer):
        pass

    def Notify(self):
        pass


class Secretary(SecretaryBase):
    def Attach(self, new_observer):
        self.observers.append(new_observer)

    def Notify(self):
        for p in self.observers:
            p.Update()


def test1():
    p = Secretary()
    s1 = StockObserver("xh", p)
    s2 = NBAObserver("wyt", p)
    p.Attach(s1)
    p.Attach(s2)
    p.action = "WARNING:BOSS "
    p.Notify()
test1()


print '---------------------------------1--------------------------------'


class ObserverBase(object):
    def update(self):
        pass


class Observer1(ObserverBase):

    def update(self):
        print "observer1 has received!"


class Observer2(ObserverBase):

    def update(self):
        print "observer2 has received!"


class Subject(object):
    def add(self, observer):
        pass

    def delete(self, observer):
        pass

    def notifyObservers(self):
        pass

    def operation(self):
        pass


class AbstractSubject(Subject):
    vector = []

    def add(self, observer):
        self.vector.append(observer)

    def delete(self, observer):
        self.vector.remove(observer)

    def notifyObservers(self):
        while(len(self.vector) > 0):
            self.vector.pop().update()


class MySubject(AbstractSubject):

    def operation(self):
        print "update self!"
        self.notifyObservers()


def ObserverTest():
    sub = MySubject()
    sub.add(Observer1())
    sub.add(Observer2())
    sub.operation()
ObserverTest()
