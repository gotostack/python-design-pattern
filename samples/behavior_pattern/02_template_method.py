print '---------------------------------1--------------------------------'


class TestPaper:
    def TestQuestion1(self):
        print "Test1: A. B. C. D."
        print "(%s)" % self.Answer1()

    def TestQuestion2(self):
        print "Test1: A. B. C. D."
        print "(%s)" % self.Answer2()

    def Answer1(self):
        return ""

    def Answer2(self):
        return ""


class TestPaperA(TestPaper):
    def Answer1(self):
        return "B"

    def Answer2(self):
        return "C"


class TestPaperB(TestPaper):
    def Answer1(self):
        return "D"

    def Answer2(self):
        return "D"


def test1():
    s1 = TestPaperA()
    s2 = TestPaperB()
    print "student 1"
    s1.TestQuestion1()
    s1.TestQuestion2()
    print "student 2"
    s2.TestQuestion1()
    s2.TestQuestion2()
test1()


print '---------------------------------1--------------------------------'


class AbstractCalculator(object):

    def calculate(self, exp, opt):
        array = self.split(exp, opt)
        return self.add(array[0], array[1])

    def add(self, num1, num2):
        pass

    def split(self, exp, opt):
        array = exp.split(opt)
        arrayInt = []
        arrayInt.append(int(array[0]))
        arrayInt.append(int(array[1]))
        return arrayInt


class Plus(AbstractCalculator):
    def add(self, num1, num2):
        return num1 + num2


def test2():
    exp = "8+8"
    cal = Plus()
    result = cal.calculate(exp, "+")
    print result
test2()
