print '---------------------------------1--------------------------------'


class Component:
    def __init__(self, strName):
        self.m_strName = strName

    def Add(self, com):
        pass

    def Display(self, nDepth):
        pass


class Leaf(Component):
    def Add(self, com):
        print "leaf can't add"

    def Display(self, nDepth):
        strtemp = ""
        for _ in range(nDepth):
            strtemp = strtemp + "-"
        strtemp = strtemp + self.m_strName
        print strtemp


class Composite(Component):
    def __init__(self, strName):
        self.m_strName = strName
        self.c = []

    def Add(self, com):
        self.c.append(com)

    def Display(self, nDepth):
        strtemp = ""
        for _ in range(nDepth):
            strtemp = strtemp + "-"
        strtemp = strtemp + self.m_strName
        print strtemp
        for com in self.c:
            com.Display(nDepth+2)


def test1():
    p = Composite("Wong")
    p.Add(Leaf("Lee"))
    p.Add(Leaf("Zhao"))
    p1 = Composite("Wu")
    p1.Add(Leaf("San"))
    p.Add(p1)
    p.Display(1)
test1()


print '---------------------------------2--------------------------------'


class TreeNode(object):
    name = ""
    parent = None
    children = []

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def add(self, node):
        self.children.append(node)

    def remove(self, node):
        self.children.remove(node)

    def getChildren(self):
        return self.children


class Tree(object):
    root = None

    def __init__(self, name):
        self.root = TreeNode(name)


def testTree():
    tree = Tree("A")
    nodeB = TreeNode("B")
    nodeC = TreeNode("C")

    nodeB.add(nodeC)
    tree.root.add(nodeB)
    print "build the tree finished!"
    print tree.root.getChildren()
testTree()
