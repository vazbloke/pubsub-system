import os
from msg_sender import Messenger
from broker_list_manager import BrokerManager
import message_utility
import log


class Subscribe:
    """
    Subscriber performs task of subscription
    """
    def subscribe(self, subscriber_mail_id, events):

        self.subscribe_phase3(subscriber_mail_id,events)
        
    def subscribe_phase3(self, subscriber_mail_id, events):
        broker_ip = BrokerManager().get_random_broker()
        msg = message_utility.get_subscriber_msg(events, subscriber_mail_id)
        log.log_to_file(broker_ip)
        Messenger().send_message(msg, broker_ip)

    def unsubscribe(self, mail_id, event):
        # Todo: send delete msg to subscriber
        pass
