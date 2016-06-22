print '---------------------------------1--------------------------------'


class Context:
    def __init__(self):
        self.input = ""
        self.output = ""


class AbstractExpression:
    def Interpret(self, context):
        pass


class Expression(AbstractExpression):
    def Interpret(self, context):
        print "terminal interpret"


class NonterminalExpression(AbstractExpression):
    def Interpret(self, context):
        print "Nonterminal interpret"


def test1():
    context = ""
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)
test1()


print '---------------------------------2--------------------------------'


class Expression2(object):
    def interpret(self, context):
        pass


class Plus(Expression2):
    def interpret(self, context):
        return context.getNum1() + context.getNum2()


class Minus(Expression2):
    def interpret(self, context):
        return context.getNum1() - context.getNum2()


class Context2(object):
    num1 = 0
    num2 = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def getNum1(self):
        return self.num1

    def setNum1(self, num1):
        self.num1 = num1

    def getNum2(self):
        return self.num2

    def setNum2(self, num2):
        self.num2 = num2


def test2():
    # 9+2-8
    result = Minus().interpret((Context2(Plus().interpret(Context2(9, 2)), 8)))
    print result
test2()
