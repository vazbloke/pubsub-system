import smtplib
import subprocess
import os
from broker_list_manager import BrokerManager
from msg_sender import Messenger
from log import log_to_file
import message_utility, sys
SENDER = "ds.project2.cse@gmail.com"
PASSWORD = "passphrase"


class Publish:
    def notify_subscribers(self, recipient, message, broker_name, subject="Email alert from CDS"):
        try:
            log_to_file(",".join(recipient)+" "+message)
            ip = subprocess.check_output(" awk 'END{print $1}' /etc/hosts ", encoding='utf-8', stderr=subprocess.STDOUT,
                                    shell=True)
            
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(SENDER, PASSWORD)
            email_text = """Subject: %s\n%s \n Broker name - %s\n Broker IP - %s""" % (subject, message, broker_name, str(ip))
            # print(email_text)
            server.sendmail(SENDER, recipient, email_text)
            server.close()

            print("Email sent to "+str(recipient), file=sys.stderr)
        except Exception as e:
            print('Something went wrong...', e)

    def publish_event(self, event, message, table='events'):
        log_to_file("publish"+event+table)
        broker_ip = BrokerManager().get_random_broker()
        msg = message_utility.get_publish_msg(event, message)
        Messenger().send_message(msg,broker_ip)
    
    def notify(self, event, message, table='events'):
        import db
        d = db.DB()
        subscriber_list = d.get_mail_list_for_event(event, table)

        if len("".join(subscriber_list)) < 6:
            print("small list to process :", "".join(subscriber_list))
        else:
            self.notify_subscribers(subscriber_list, message, table)
        

def main():
    e = Publish()
    e.notify_subscribers(["pratik.vagyani2nov@gmail.com"],"Shift available on 10/12, 5-9PM", "broker k")


if __name__ == '__main__':
    main()
