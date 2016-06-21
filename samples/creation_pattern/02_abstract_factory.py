class Sender(object):

    def Send(self):
        raise NotImplementedError()


class MailSender(Sender):

    def Send(self):
        print "this is mail sender!"


class SmsSender(Sender):

    def Send(self):
        print "this is sms sender!"


class Provider(object):

    def produce(self):
        raise NotImplementedError()


class SendMailFactory(Provider):

    def produce(self):
        return MailSender()


class SendSmsFactory(Provider):

    def produce(self):
        return SmsSender()


sms_provider = SendSmsFactory()
sender = sms_provider.produce()
sender.Send()

mail_provider = SendMailFactory()
sender = mail_provider.produce()
sender.Send()
