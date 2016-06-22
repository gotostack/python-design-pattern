print '---------------------------------1--------------------------------'


class Person:
    def Accept(self, visitor):
        pass


class Man(Person):
    def Accept(self, visitor):
        visitor.GetManConclusion(self)


class Woman(Person):
    def Accept(self, visitor):
        visitor.GetWomanConclusion(self)


class Action:
    def GetManConclusion(self, concreteElementA):
        pass

    def GetWomanConclusion(self, concreteElementB):
        pass


class Success(Action):
    def GetManConclusion(self, concreteElementA):
        print "A man"

    def GetWomanConclusion(self, concreteElementB):
        print "A woman"


class Failure(Action):
    def GetManConclusion(self, concreteElementA):
        print "A failed man"

    def GetWomanConclusion(self, concreteElementB):
        print "A failed woman"


class ObjectStructure:
    def __init__(self):
        self.plist = []

    def Add(self, p):
        self.plist = self.plist+[p]

    def Display(self, act):
        for p in self.plist:
            p.Accept(act)


def test1():
    os = ObjectStructure()
    os.Add(Man())
    os.Add(Woman())
    sc = Success()
    os.Display(sc)
    fl = Failure()
    os.Display(fl)
test1()


print '---------------------------------2--------------------------------'


class Visitor(object):
    def visit(self, sub):
        pass


class MyVisitor(Visitor):
    def visit(self, sub):
        print "visit the subject: " + sub.getSubject()


class Subject(object):
    def accept(self, visitor):
        pass

    def getSubject(self):
        pass


class MySubject(Subject):

    def accept(self, visitor):
        visitor.visit(self)

    def getSubject(self):
        return "love"


def test2():
        visitor = MyVisitor()
        sub = MySubject()
        sub.accept(visitor)
test2()
