import os
import random


class BrokerManager:
    """
    This class maintains list of broker in network.
    """
    def __init__(self):
        self.broker_list=[]

    def list_broker(self):
        self.broker_list = os.environ['BROKERLIST'].split(',')
        #with open(os.path.join('info', 'broker_list.txt')) as f:
        #    self.broker_list = [line.strip() for line in f.readlines() if line.strip() is not ""]

    def get_random_broker(self):
        self.list_broker()
        id_ = random.randint(0, len(self.broker_list)-1)
        return self.broker_list[id_]


def main():
    b = BrokerManager()
    b.get_random_broker()


if __name__ == '__main__':
    main()

