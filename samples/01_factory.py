class Sender(object):

    def Send(self):
        raise NotImplementedError()


class MailSender(Sender):

    def Send(self):
        print "this is mail sender!"


class SmsSender(Sender):

    def Send(self):
        print "this is sms sender!"


# Normal factory
class SendFactory(object):

    def produce(self, stype):
        if "mail" == stype:
            return MailSender()
        elif "sms" == stype:
            return SmsSender()
        else:
            print "Please input a valid sender type:"
            return None


factory = SendFactory()
sender = factory.produce("sms")
sender.Send()

sender = factory.produce("mail")
sender.Send()


# Multiple Factory
class SendMultipleFactory(object):

    def produceMail(self):
        return MailSender()

    def produceSms(self):
        return SmsSender()

factory = SendMultipleFactory()
sender = factory.produceMail()
sender.Send()

sender = factory.produceSms()
sender.Send()


# Static Factory
class SendStaticFactory(object):

    @staticmethod
    def produceMail():
        return MailSender()

    @staticmethod
    def produceSms():
        return SmsSender()


sender = SendStaticFactory.produceMail()
sender.Send()

sender = SendStaticFactory.produceSms()
sender.Send()
