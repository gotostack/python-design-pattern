print '---------------------------------1--------------------------------'


class Request:
    def __init__(self, tcontent, tnum):
        self.content = tcontent
        self.num = tnum


class Manager:
    def __init__(self, temp):
        self.name = temp

    def SetSuccessor(self, temp):
        self.manager = temp

    def GetRequest(self, req):
        pass


class CommonManager(Manager):
    def GetRequest(self, req):
        if req.num >= 0 and req.num < 10:
            print "%s handled %d request." % (self.name, req.num)
        else:
            self.manager.GetRequest(req)


class MajorDomo(Manager):
    def GetRequest(self, req):
        if req.num >= 10:
            print "%s handled %d request." % (self.name, req.num)


def test1():
    common = CommonManager("Zhang")
    major = MajorDomo("Lee")
    common.SetSuccessor(major)
    req = Request("rest", 33)
    common.GetRequest(req)
    req2 = Request("salary", 3)
    common.GetRequest(req2)
test1()


print '---------------------------------2--------------------------------'


class Handler(object):
    def operator(self):
        pass


class AbstractHandler(Handler):
    handler = None

    def getHandler(self):
        return self.handler

    def setHandler(self, handler):
        self.handler = handler


class MyHandler(AbstractHandler, Handler):

    name = ""

    def __init__(self, name):
        self.name = name

    def operator(self):
        print self.name + " deal!"
        handler = self.getHandler()
        if handler:
            handler.operator()


def test2():
    h1 = MyHandler("h1")
    h2 = MyHandler("h2")
    h3 = MyHandler("h3")

    h1.setHandler(h2)
    h2.setHandler(h3)

    h1.operator()

test2()
