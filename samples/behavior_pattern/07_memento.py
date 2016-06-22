print '---------------------------------1--------------------------------'


class Originator:
    def __init__(self):
        self.state = ""

    def Show(self):
        print self.state

    def CreateMemo(self):
        return Memo(self.state)

    def SetMemo(self, memo):
        self.state = memo.state


class Memo:
    state = ""

    def __init__(self, ts):
        self.state = ts


class Caretaker:
    memo = ""


def test1():
    on = Originator()
    on.state = "on"
    on.Show()
    c = Caretaker()
    c.memo = on.CreateMemo()
    on.state = "off"
    on.Show()
    on.SetMemo(c.memo)
    on.Show()
test1()

print '---------------------------------2--------------------------------'


class Original(object):
    value = ""

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def createMemento(self):
        return Memento(self.value)

    def restoreMemento(self, memento):
        self.value = memento.getValue()


class Memento(object):
    value = ""

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


class Storage(object):
    memento = None

    def __init__(self, memento):
        self.memento = memento

    def getMemento(self):
        return self.memento

    def setMemento(self, memento):
        self.memento = memento


def test2():
    # original class
    origi = Original("egg")

    #  create Memento
    storage = Storage(origi.createMemento())

    # change origin class state
    print "origin state: " + origi.getValue()
    origi.setValue("niu")
    print "changed state: " + origi.getValue()

    # set old state back
    origi.restoreMemento(storage.getMemento())
    print "restored state: " + origi.getValue()
test2()
