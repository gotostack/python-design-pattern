print '---------------------------------1--------------------------------'


class CashSuper:
    def AcceptCash(self, money):
        return 0


class CashNormal(CashSuper):
    def AcceptCash(self, money):
        return money


class CashRebate(CashSuper):
    discount = 0

    def __init__(self, ds):
        self.discount = ds

    def AcceptCash(self, money):
        return money * self.discount


class CashReturn(CashSuper):
    total = 0
    ret = 0

    def __init__(self, t, r):
        self.total = t
        self.ret = r

    def AcceptCash(self, money):
        if (money >= self.total):
            return money - self.ret
        else:
            return money


class CashContext:
    def __init__(self, csuper):
        self.cs = csuper

    def GetResult(self, money):
        return self.cs.AcceptCash(money)


def test1():
    money = input("money:")
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300, 100))
    stype = input("Strategy: "
                  "[1]for normal, "
                  "[2]for 80% discount, "
                  "[3]for 300 -100: ")
    if stype in strategy:
        cc = strategy[stype]
    else:
        print "Unknow type. Use normal mode."
        cc = strategy[1]
    print "you will pay: %d" % (cc.GetResult(money))

test1()


print '---------------------------------2--------------------------------'


class ICalculator(object):
    def calculate(self, exp):
        pass


class AbstractCalculator(object):
    def split(self, exp, opt):
        array = exp.split(opt)
        print array
        arrayInt = []
        arrayInt.append(int(array[0]))
        arrayInt.append(int(array[1]))
        return arrayInt


class Plus(AbstractCalculator, ICalculator):
    def calculate(self, exp):
        arrayInt = self.split(exp, "+")
        return arrayInt[0] + arrayInt[1]


class Minus(AbstractCalculator, ICalculator):

    def calculate(self, exp):
        arrayInt = self.split(exp, "-")
        return arrayInt[0] - arrayInt[1]


class Multiply(AbstractCalculator, ICalculator):
    def calculate(self, exp):
        arrayInt = self.split(exp, "*")
        return arrayInt[0] * arrayInt[1]


def StrategyTest():
    exp = "2+8"
    cal = Plus()
    result = cal.calculate(exp)
    print "Result: ", result

    exp = "2-8"
    cal = Minus()
    result = cal.calculate(exp)
    print "Result: ", result

    exp = "2*8"
    cal = Multiply()
    result = cal.calculate(exp)
    print "Result: ", result
StrategyTest()
