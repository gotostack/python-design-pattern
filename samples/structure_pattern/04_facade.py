print '---------------------------------1--------------------------------'


class SubSystemOne:
    def MethodOne(self):
        print "SubSysOne"


class SubSystemTwo:
    def MethodTwo(self):
        print "SubSysTwo"


class SubSystemThree:
    def MethodThree(self):
        print "SubSysThree"


class SubSystemFour:
    def MethodFour(self):
        print "SubSysFour"


class Facade:
    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()

    def MethodA(self):
        print "MethodA"
        self.one.MethodOne()
        self.two.MethodTwo()
        self.four.MethodFour()

    def MethodB(self):
        print "MethodB"
        self.two.MethodTwo()
        self.three.MethodThree()


def test1():
    facade = Facade()
    facade.MethodA()
    facade.MethodB()
test1()


print '---------------------------------2--------------------------------'


class CPU(object):
    def startup(self):
        print "cpu startup!"

    def shutdown(self):
        print "cpu shutdown!"


class Memory(object):
    def startup(self):
        print "memory startup!"

    def shutdown(self):
        print "memory shutdown!"


class Disk(object):
    def startup(self):
        print "disk startup!"

    def shutdown(self):
        print "disk shutdown!"


class Computer(object):
    cpu = None
    memory = None
    disk = None

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.disk = Disk()

    def startup(self):
        print "start the computer!"
        self.cpu.startup()
        self.memory.startup()
        self.disk.startup()
        print "start computer finished!"

    def shutdown(self):
        print "begin to close the computer!"
        self.cpu.shutdown()
        self.memory.shutdown()
        self.disk.shutdown()
        print "computer closed!"


def User():
    computer = Computer()
    computer.startup()
    computer.shutdown()
User()
