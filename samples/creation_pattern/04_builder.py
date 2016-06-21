class Sender(object):

    def Send(self):
        raise NotImplementedError()


class MailSender(Sender):

    def Send(self):
        print "this is mail sender!"


class SmsSender(Sender):

    def Send(self):
        print "this is sms sender!"


# Builder
class Builder(object):
    seq = []

    def SendEmailViaSms(self):
        mail = MailSender()
        sms = SmsSender()
        self.seq.append(mail)
        self.seq.append(sms)

    def Send(self):
        self.SendEmailViaSms()
        for item in self.seq:
            item.Send()

builder = Builder()
builder.Send()


print "---------------------2-----------------------"


class Person:
    def CreateHead(self):
        pass

    def CreateHand(self):
        pass

    def CreateBody(self):
        pass

    def CreateFoot(self):
        pass


class ThinPerson(Person):
    def CreateHead(self):
        print "thin head"

    def CreateHand(self):
        print "thin hand"

    def CreateBody(self):
        print "thin body"

    def CreateFoot(self):
        print "thin foot"


class ThickPerson(Person):
    def CreateHead(self):
        print "thick head"

    def CreateHand(self):
        print "thick hand"

    def CreateBody(self):
        print "thick body"

    def CreateFoot(self):
        print "thick foot"


class Director:
    def __init__(self, temp):
        self.p = temp

    def Create(self):
        self.p.CreateHead()
        self.p.CreateBody()
        self.p.CreateHand()
        self.p.CreateFoot()

p = ThinPerson()
d = Director(p)
d.Create()
