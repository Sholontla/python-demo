import time
import numpy as np
import pandas as pd
from faker import Faker
from datetime import timedelta, datetime

from pydantic.tools import T

from schemas import User, UserInteraction, ProductCategory, Discount, ProductInventory, Product, OrderDetails, PaymentDetails, OrderItems, ShoppingSession, CartItem, UserAddress, UserPayment
from postgresql_connection import Sql

class SalesDataGenerator:
    def __init__(self, seconds):
        self.faker = Faker()
        self.seconds = seconds
        self.Sql = Sql()
    
    def generate_credit_card_fake(self):   
        credit_card1 = np.random.randint(9, size=(4))
        credit_card2 = np.random.randint(9, size=(4))
        credit_card3 = np.random.randint(9, size=(4))
        credit_card4 = np.random.randint(9, size=(4))
        credit_card1 = np.array_str(credit_card1).replace(" ", "").replace("[", "").replace("]", "")
        credit_card2 = np.array_str(credit_card2).replace(" ", "").replace("[", "").replace("]", "")
        credit_card3 = np.array_str(credit_card3).replace(" ", "").replace("[", "").replace("]", "")
        credit_card4 = np.array_str(credit_card4).replace(" ", "").replace("[", "").replace("]", "")
        credit_card_format = credit_card1 + " " + credit_card2 + " " + credit_card3 + " " + credit_card4
        yield credit_card_format

    def user_generator(self):   
        for _ in range(15000):
            credit_card1 = np.random.randint(9, size=(4))
            credit_card2 = np.random.randint(9, size=(4))
            credit_card3 = np.random.randint(9, size=(4))
            credit_card4 = np.random.randint(9, size=(4))
            credit_card1 = np.array_str(credit_card1).replace(" ", "").replace("[", "").replace("]", "")
            credit_card2 = np.array_str(credit_card2).replace(" ", "").replace("[", "").replace("]", "")
            credit_card3 = np.array_str(credit_card3).replace(" ", "").replace("[", "").replace("]", "")
            credit_card4 = np.array_str(credit_card4).replace(" ", "").replace("[", "").replace("]", "")
            credit_card_format = credit_card1 + " " + credit_card2 + " " + credit_card3 + " " + credit_card4
            fake_username = self.faker.user_name()
            fake_phone = self.faker.phone_number()
            fake_email = self.faker.email()
            fake_tc = credit_card_format

            df_dict = {"username": [f"{fake_username}"], "phone": [fake_phone], "email": [f"{fake_email}"], "credit_card_encrypt": [f"{fake_tc}"], "credit_card_mask": [f"{fake_tc}"]}
            df = pd.DataFrame.from_dict(df_dict)
            self.Sql.sql_append_data(df, "citi_data_testing")


    def user_interaction_generator(self):
        for _ in range(3585):
            fake_phone = self.faker.phone_number()
            userame_first = self.faker.first_name()[0:3]
            userame_last = self.faker.last_name()[0:3]
            df_dict = {"requested_email": None, "username": f"{userame_first}-{userame_last}", "phone": fake_phone, "email": f"{userame_first.lower()}-{userame_last.lower()}@organization-example.com", "created": datetime.now(), "time": datetime.now()}
            self.MongoConnection.add_many_elements_user_interation_collection(df_dict)


    def product_inventory_generator(self):
        quantity_generator = np.random.randint(50, size=(1))
        yield ProductInventory ( 
            quantity = quantity_generator,
            created = datetime.now(),
        )

    def discount_generator(self):
        descount_generator = np.random.randint(50, size=(1))
        bool_generator = self.faker.boolean()
        yield Discount ( 
            desc = descount_generator,
            active = bool_generator,
            created = datetime.now()
        )

    def product(self):
        register_generator = self.faker.bban()
        price_generator = np.random.uniform(5.0, 775.8)
        yield Product(
            sku = register_generator,
            category_id = self.product_category_generator(),
            inventory_id = self.product_inventory_generator(),
            price = price_generator,
            disct_id = self.discount_generator(),
            created = datetime.now()
        )

    def order_details(self):
        OrderDetails(
            user_id = User,
            total = float,
            created = datetime.now()
        )



print(SalesDataGenerator(1).user_generator())


