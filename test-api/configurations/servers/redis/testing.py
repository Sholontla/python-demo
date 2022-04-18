from faker import Faker
from pprint import pprint
import time
import asyncio

fake = Faker()
Faker.seed(0)

# while True:
#     for _ in range(5):    
#         pprint({"address": f"{fake.address()}", "name": f"{fake.name()}", "lastName": f"{fake.last_name()}", "job": f"{fake.job()}", "phoneNumber": f"{fake.phone_number()}"})
#         time.sleep(2)

def testing_data(active):
    while active: 
        for _ in range(5):
            yield fake.profile()
            time.sleep(5)


# if __name__ == "__main__":
#     for i in testing_data(True):
#         pprint(i)
    