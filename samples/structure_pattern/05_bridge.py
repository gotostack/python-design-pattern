print '---------------------------------1--------------------------------'


class HandsetSoft(object):
    def Run(self):
        pass


class HandsetGame(HandsetSoft):
    def Run(self):
        print "Game"


class HandsetAddressList(HandsetSoft):
    def Run(self):
        print "Address List"


class HandsetBrand(object):
    def __init__(self):
        self.m_soft = None

    def SetHandsetSoft(self, temp):
        self.m_soft = temp

    def Run(self):
        pass


class HandsetBrandM(HandsetBrand):
    def Run(self):
        if self.m_soft:
            print "BrandM"
            self.m_soft.Run()


class HandsetBrandN(HandsetBrand):
    def Run(self):
        if self.m_soft:
            print "BrandN"
            self.m_soft.Run()


def test1():
    brand = HandsetBrandM()
    brand.SetHandsetSoft(HandsetGame())
    brand.Run()
    brand.SetHandsetSoft(HandsetAddressList())
    brand.Run()

test1()


print '---------------------------------2--------------------------------'


class Sourceable(object):
    def method(self):
        pass


class SourceSub1(Sourceable):
    def method(self):
        print "this is the first sub!"


class SourceSub2(Sourceable):
    def method(self):
        print "this is the second sub!"


class Bridge(object):
    source = None

    def method(self):
        self.source.method()

    def getSource(self):
        return self.source

    def setSource(self, source):
        self.source = source


class MyBridge(Bridge):
    def method(self):
        self.getSource().method()


def BridgeTest():
    bridge = MyBridge()

    source1 = SourceSub1()
    bridge.setSource(source1)
    bridge.method()

    source2 = SourceSub2()
    bridge.setSource(source2)
    bridge.method()
BridgeTest()
