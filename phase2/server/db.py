import psycopg2, os

USER = 'postgres'
PASSWORD = 'root'
HOST = os.environ['DB_HOST']
PORT = '5432'


class DB:
    def __init__(self):
        self.conn = None

    def get_connection(self):
        self.conn = psycopg2.connect(database="sample", user=USER, host=HOST, password=PASSWORD, port=PORT)
        return self.conn.cursor()

    def close(self):
        self.conn.close()

    def is_event_exists(self, event, cursor, table='events'):
        cursor.execute("select count(1) from " + table + " where event_type='" + event + "';")
        res = cursor.fetchall()
        if int(res[0])>0:
            return True
        return False

    def remove_subscriber(self,mail_id,events):
        events.split(';')
        #TODOwrite code to remove subscriber from email list

    def add_subscriber(self,subscriber_mail_id, interest, table="events"):
        print(subscriber_mail_id,interest)
        cursor = self.get_connection()
        interests = interest.split(';')
        for intr in interests:
            if intr.strip() == "":
                continue
            sql = "update "+table+" set subscriber_email_list=concat(subscriber_email_list,';','" + \
                  subscriber_mail_id + "') " \
                  "where event_type='" + intr + "' " + \
                  " AND subscriber_email_list NOT LIKE '%" + subscriber_mail_id + "%';"
            print(sql)
            cursor.execute(sql)
            self.conn.commit()
        self.close()

    def show_events(self, table='events'):
        cursor = self.get_connection()
        cursor.execute("select * from " + table + ";")
        res = cursor.fetchall()
        for rows in res:
            print(rows)
        self.close()

    def get_mail_list_for_event(self,event, table='events'):
        cursor = self.get_connection()
        cursor.execute("select subscriber_email_list from " + table + " where event_type='"+event+"';")
        res = cursor.fetchall()
        sub_list = res[0][0]
        self.close()
        return sub_list.split(";")


def main():
    d = DB()
    d.add_subscriber("emzdail@google.com","putnam;pistachio")
    d.show_events()

if __name__ == '__main__':
    main()
