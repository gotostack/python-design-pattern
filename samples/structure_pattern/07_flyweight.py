print '---------------------------------1--------------------------------'


class WebSite:
    def Use(self):
        pass


class ConcreteWebSite(WebSite):
    def __init__(self, strName):
        self.name = strName

    def Use(self, user):
        print "Website type:%s,user:%s" % (self.name, user)


class UnShareWebSite(WebSite):
    def __init__(self, strName):
        self.name = strName

    def Use(self, user):
        print "UnShare Website type:%s,user:%s" % (self.name, user)


class WebFactory:
    def __init__(self):
        test = ConcreteWebSite("test")
        self.webtype = {"test": test}
        self.count = {"test": 0}

    def GetWeb(self, webtype):
        if webtype not in self.webtype:
            temp = ConcreteWebSite(webtype)
            self.webtype[webtype] = temp
            self.count[webtype] = 1
        else:
            temp = self.webtype[webtype]
            self.count[webtype] = self.count[webtype]+1
        return temp

    def GetCount(self):
        for key in self.webtype:
            print "type: %s, count:%d " % (key, self.count[key])


def test1():
    f = WebFactory()
    ws = f.GetWeb("blog")
    ws.Use("Lee")
    ws2 = f.GetWeb("show")
    ws2.Use("Jack")
    ws3 = f.GetWeb("blog")
    ws3.Use("Chen")
    ws4 = UnShareWebSite("TEST")
    ws4.Use("Mr.Q")
    print f.webtype
    f.GetCount()
test1()


print '---------------------------------2--------------------------------'


class DriverManager(object):
    def getConnection(self, url, username, password):
        return 'a connection'


class ConnectionPool(object):
    pool = []

    url = "jdbc:mysql://localhost:3306/test"
    username = "root"
    password = "root"
    driverClassName = "com.mysql.jdbc.Driver"

    poolSize = 100
    instance = None
    conn = None

    def __init__(self):
        for _ in range(100):
            manager = DriverManager()
            conn = manager.getConnection(self.url,
                                         self.username,
                                         self.password)
            self.pool.append(conn)

    def release(self, conn):
        self.pool.append(conn)

    def getConnection(self):
        if len(self.pool) > 0:
            conn = self.pool.pop()
            return conn


def testConnectPool():
    pool = ConnectionPool()
    conn = pool.getConnection()
    print conn
    for _ in range(100):
        conn2 = pool.getConnection()
        if not conn2:
            print "pool has no available connection"
    conn = pool.release(conn)
    conn = pool.getConnection()
    print conn
    conn = pool.getConnection()
    print conn
testConnectPool()
