print '---------------------------------1--------------------------------'


class State:
    def WirteProgram(self):
        pass


class Work:
    def __init__(self):
        self.hour = 9
        self.current = ForenoonState()

    def SetState(self, temp):
        self.current = temp

    def WriteProgram(self):
        self.current.WriteProgram(self)


class NoonState(State):
    def WriteProgram(self, w):
        print "noon working"
        if w.hour < 13:
            print "fun."
        else:
            print "need to rest."


class ForenoonState(State):
    def WriteProgram(self, w):
        if w.hour < 12:
            print "morning working"
            print "energetic"
        else:
            w.SetState(NoonState())
            w.WriteProgram()


def test1():
    mywork = Work()
    mywork.hour = 9
    mywork.WriteProgram()
    mywork.hour = 14
    mywork.WriteProgram()
test1()


print '---------------------------------2--------------------------------'


class State2(object):
    value = ""

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def method1(self):
        print "execute the first opt!"

    def method2(self):
        print "execute the second opt!"


class Context(object):
    state = None

    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def method(self):
        if self.state.getValue() == "state1":
            self.state.method1()
        elif self.state.getValue() == "state2":
            self.state.method2()


def test2():
    state = State2()
    context = Context(state)

    # set state1
    state.setValue("state1")
    context.method()

    # set state2
    state.setValue("state2")
    context.method()
test2()
