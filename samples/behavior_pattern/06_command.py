print '---------------------------------1--------------------------------'


class Barbucer:
    def MakeMutton(self):
        print "Mutton"

    def MakeChickenWing(self):
        print "Chicken Wing"


class Command:
    def __init__(self, temp):
        self.receiver = temp

    def ExecuteCmd(self):
        pass


class BakeMuttonCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeMutton()


class ChickenWingCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeChickenWing()


class Waiter:
    def __init__(self):
        self.order = []

    def SetCmd(self, command):
        self.order.append(command)
        print "Add Order"

    def Notify(self):
        for cmd in self.order:
            # self.order.remove(cmd)
            # lead to a bug
            cmd.ExecuteCmd()


def test1():
    barbucer = Barbucer()
    cmd = BakeMuttonCmd(barbucer)
    cmd2 = ChickenWingCmd(barbucer)
    girl = Waiter()
    girl.SetCmd(cmd)
    girl.SetCmd(cmd2)
    girl.Notify()
test1()


print '---------------------------------2--------------------------------'


class Command2(object):
    def exe(self):
        pass


class MyCommand(Command2):

    receiver = None

    def __init__(self, receiver):
        self.receiver = receiver

    def exe(self):
        self.receiver.action()


class Receiver(object):
    def action(self):
        print "command received!"


class Invoker(object):
    command = None

    def __init__(self, command):
        self.command = command

    def action(self):
        self.command.exe()


def test2():
    receiver = Receiver()
    cmd = MyCommand(receiver)
    invoker = Invoker(cmd)
    invoker.action()
test2()
