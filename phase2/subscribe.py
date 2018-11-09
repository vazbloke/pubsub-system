import db


class Subscribe:
    def subscribe(self, subscriber_mail_id, events):
        database = db.DB()
        database.add_subscriber(subscriber_mail_id, events)

    def unsubscribe(self, mail_id, event):
        database = db.DB()
        database.remove_subscriber(mail_id, event)

