import smtplib
import subprocess

SENDER = "ds.project2.cse@gmail.com"
PASSWORD = "passphrase"


class Publish:
    def notify_subscribers(self, recipient, message, subject="Email alert from CDS"):
        try:

            ip = subprocess.check_output(" awk 'END{print $1}' /etc/hosts ", encoding='utf-8', stderr=subprocess.STDOUT,
                                    shell=True).strip().replace(".", "")
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(SENDER, PASSWORD)
            email_text = """Subject: %s\n%s""" % (subject, message)
            email_text += "\n message from " + str(ip)
            server.sendmail(SENDER, recipient, email_text)
            server.close()

            print('Email sent!')
        except Exception as e:
            print('Something went wrong...', e)

    def publish_event(self, event, message, table='events'):
        import db
        d = db.DB()
        subscriber_list = d.get_mail_list_for_event(event, table)

        if len("".join(subscriber_list)) < 6:
            print("small list to process :", "".join(subscriber_list))
        else:
            self.notify_subscribers(subscriber_list, message)


def main():
    e = Publish()
    e.notify_subscribers(["pratikap@buffalo.edu","pratik.vagyani2nov@gmail.com"],"hello")


if __name__ == '__main__':
    main()
