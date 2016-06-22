print '---------------------------------1--------------------------------'


class Mediator:
    def Send(self, message, col):
        pass


class Colleague:
    def __init__(self, temp):
        self.mediator = temp


class Colleague1(Colleague):
    def Send(self, message):
        self.mediator.Send(message, self)

    def Notify(self, message):
        print "Colleague1 get a message:%s" % message


class Colleague2(Colleague):
    def Send(self, message):
        self.mediator.Send(message, self)

    def Notify(self, message):
        print "Colleague2 get a message:%s" % message


class ConcreteMediator(Mediator):
    def Send(self, message, col):
        if col == self.col1:
            self.col2.Notify(message)
        else:
            self.col1.Notify(message)


def test1():
    m = ConcreteMediator()
    col1 = Colleague1(m)
    col2 = Colleague2(m)
    m.col1 = col1
    m.col2 = col2
    col1.Send("How are you?")
    col2.Send("Fine.")
test1()


print '---------------------------------2--------------------------------'


class Mediator2(object):
    def createMediator(self):
        pass

    def workAll(self):
        pass


class MyMediator2(Mediator2):
    user1 = None
    user2 = None

    def getUser1(self):
        return self.user1

    def getUser2(self):
        return self.user2

    def createMediator(self):
        self.user1 = User1(self)
        self.user2 = User2(self)

    def workAll(self):
        self.user1.work()
        self.user2.work()


class UserBase(object):
    mediator = None

    def __init__(self, mediator):
        self.mediator = mediator

    def getMediator(self):
        return self.mediator

    def work(self):
        print "user1 exe!"


class User1(UserBase):
    def __init__(self, mediator):
        super(User1, self).__init__(mediator)

    def work(self):
        print "user1 exe!"


class User2(UserBase):
    def __init__(self, mediator):
        super(User2, self).__init__(mediator)

    def work(self):
        print "user2 exe!"


def test2():
    mediator = MyMediator2()
    mediator.createMediator()
    mediator.workAll()
test2()
