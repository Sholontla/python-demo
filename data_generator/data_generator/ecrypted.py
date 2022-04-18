from passlib.context import CryptContext
from multiprocessing.pool import ThreadPool
from functools import partial

class EncryiptionData:
    def __init__(self):
        self.crypto_pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcryptElement(self, element: str):
        hashed_element = self.crypto_pwd.hash(element)
        return hashed_element

    def verify(self, hashed_element, plain_element):
        return self.crypto_pwd.verify(plain_element, hashed_element)

    def threadEncryptionElement(self, element):
        with ThreadPool(len(element)) as processing_pool:
            result_list = processing_pool.map(self.bcryptElement, element)
        return result_list