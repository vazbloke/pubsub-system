import smtplib, sys

SENDER = "ds.project2.cse@gmail.com"
PASSWORD = "passphrase"


class Publish:
    def notify_subscribers(self, recipient, message, subject="Email alert from CDS"):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(SENDER, PASSWORD)
            email_text = """Subject: %s\n%s""" % (subject, message)
            print(email_text)
            server.sendmail(SENDER, recipient, email_text)
            server.close()

            print('Email sent to '+ str(recipient), file=sys.stderr)
        except Exception as e:
            print('Something went wrong...',e)

    def publish_event(self, event, message):
        import db
        d = db.DB()

        subscriber_list = d.get_mail_list_for_event(event)
        self.notify_subscribers(subscriber_list, message)


def main():
    e = Publish()
    e.notify_subscribers(["pratikap@buffalo.edu","pratik.vagyani2nov@gmail.com"],"hello")


if __name__ == '__main__':
    main()
