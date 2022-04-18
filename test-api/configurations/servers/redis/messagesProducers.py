import redis
import numpy as np
import pandas as pd
from datetime import datetime
from testing import testing_data

class Generate_Data_Redis_Messages:
    def __init__(self):
        self.testing_data = testing_data(True)

    def generate_test_data(self, size: int, days, frequence):
        return pd.DataFrame({
            'clients': [
            f'Task {i + 1}'
            for i in range(size)
            ],
            'category': [
            np.random.choice(list(self.CATEGOIRES))
            for i in range(size)
            ],
            'sub_category': [
            np.random.choice(list(self.SUBCTEGORIES))
            for i in range(size)
            ],
            'products': [
            np.random.choice(list(self.PRODUCTS))
            for i in range(size)
            ],
            'sell_channel': [
            np.random.choice(list(self.CHANNELS))
            for i in range(size)
            ],
            'time_purchase': [
            pd.date_range(start=datetime.now(), periods=days, freq=frequence).to_list()[0]
            for _ in range(size)
            ],
        })

    def redis_publishers_messages(self):
        # data_dict = self.generate_test_data()
        messages = self.testing_data
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        publisher = redis.Redis(connection_pool=pool, decode_responses=True)
        channel = "api1"
        for i in messages:
            publisher.publish(channel, f"{i}")


if __name__ == '__main__':
    print("------------- CLIENT SERVER RUNNING --------------")
    data = Generate_Data_Redis_Messages()
    print(data.redis_publishers_messages())