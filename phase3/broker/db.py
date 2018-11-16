import psycopg2, time, os

USER = 'postgres'
PASSWORD = 'root'
HOST = os.environ['DB_HOST']
PORT = '5432'

"""
Schema:
    Table: events
            event_type (varchar) : name of stations
            subscriber_email_list (varchar): list of subscribers semi-colon separated
    create table events(event_type varchar, subscriber_email_list varchar, primary key event_type);
    insert into events select 'fowl play',''
    insert into events select 'stacker',''
    insert into events select 'edgyveggy',''
    insert into events select '',''
    
"""

MAX_CHECK=10


class DB:
    """
    Deals with db aspect of project
    """
    def __init__(self):
        self.conn = None
        self.wait_till_db_ready()
    
    def wait_till_db_ready(self):
        global MAX_CHECK
        for i in range(MAX_CHECK):
            try:
                self.get_connection()
                self.close()
                return True
            except:
                print("Unable to connect. Trying again.")
                time.sleep(5)
                
        

    def create_table_if_not_exists(self, table):
        sql = "create table if not exists " + table + " (event_type varchar, subscriber_email_list varchar, primary key( event_type));"
        cur = self.get_connection()
        cur.execute(sql)
        self.commit_close()

    def get_connection(self):
        self.conn = psycopg2.connect(database="sample", user=USER, password=PASSWORD, host=HOST, port=PORT)
        return self.conn.cursor()

    def commit_close(self):
        self.conn.commit()
        self.close()

    def close(self):
        self.conn.close()

    def is_event_exists(self, event, cursor, table='events'):
        cursor.execute("select count(1) from " + table + " where event_type='" + event + "';")
        res = cursor.fetchall()
        if int(res[0]) > 0:
            return True
        return False

    def remove_subscriber(self,mail_id,events,table="events"):
        events = events.split(';')
        cur = self.get_connection()
        for event in events:
            sql = "select subscriber_email_list from " + table + " e where e.event_type='" + event + "';"
            print(sql)
            cur.execute(sql)
            res = cur.fetchall()
            if len(res) > 0:
                email_list = str(res[0][0])
                email_list = email_list.replace(mail_id,"").replace(";;",";")

                sql = "update  " + table + "  set subscriber_email_list ='" + email_list + "' where event_type='" \
                      + event + "';"
                print(sql)
                cur.execute(sql)
        self.commit_close()
        #TODOwrite code to remove subscriber from email list

    def add_subscriber(self,subscriber_mail_id, interest, table="events"):
        cursor = self.get_connection()
        interests = interest.split(';')
        for intr in interests:
            if intr.strip() == "":
                continue
            print("subscription for ",intr,table)

            sql = "select count(1) from " + table + " where event_type='" + intr + "' ;"
            cursor.execute(sql)
            s=cursor.fetchall()
            if s[0][0] > 0:
                print(" -------------- insert event if exists")

                sql = "update  "+table+" set  subscriber_email_list=concat(subscriber_email_list,';','" + \
                      subscriber_mail_id + "') " \
                      "where event_type='" + intr + "' " + \
                      " AND subscriber_email_list NOT LIKE '%" + subscriber_mail_id + "%'"
                cursor.execute(sql)
                self.conn.commit()


            else:
                print("# -------------- insert event if not exists")
                print("inserting new event,",intr)
                sql = "insert into " + table + " select '" + intr + "' , '" + subscriber_mail_id + "';"
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

    def get_mail_list_for_event(self, event, table='events'):
        cursor = self.get_connection()
        cursor.execute("select subscriber_email_list as mail_list from " + table + " where event_type='"+event+"';")
        res = cursor.fetchall()
        print(len(res))
        if len(res) > 0:
            sub_list = res[0][0]
            self.close()
            return sub_list.split(";")
        return ""


def main():
    d = DB()
    d.remove_subscriber('email2@google.com','pistachio')
    d.show_events()

if __name__ == '__main__':
    main()
