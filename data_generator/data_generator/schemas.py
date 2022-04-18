from typing import Any, List, Dict, Optional, Tuple
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from pydantic import Field
from datetime import timedelta, datetime
from pprint import pprint

# ---------------------------------------------------------------------------------------------
class User(BaseModel): 
    username: str
    phone: str
    email: str
    created: datetime

class UserInteraction(BaseModel):
    requested_id = int
    requested_email = str
    user_id = int
    username = str 
    phone = str
    email = str
    created = datetime
    time = datetime

class ProductCategory(BaseModel):
    id_product: int
    created: datetime

class ProductInventory(BaseModel):
    quantity: int
    created: datetime

class Discount(BaseModel):
    desc: int
    active: bool
    created: datetime

class Product(BaseModel):
    sku: str
    category_id: ProductCategory
    inventory_id: ProductInventory
    price: float
    disct_id: Discount
    created: datetime

class OrderDetails(BaseModel):
    user_id: User
    total: float
    created: datetime

class PaymentDetails(BaseModel): 
    order_id: OrderDetails
    amount: int
    provider: str
    status: bool
    created: datetime

class OrderItems(BaseModel): 
    order_id: OrderDetails
    product_id: Product
    quantity: int
    created: datetime

class ShoppingSession(BaseModel): 
    user_id: User
    total: int
    created: datetime

class CartItem(BaseModel): 
    session_id: ShoppingSession
    product_id: Product
    quantity: int
    created: datetime

class UserAddress(BaseModel): 
    user_id: User
    UserAddresscity: int
    zip_code: int
    country: int
    phone: int
    mobile: int

class UserPayment(BaseModel):
    user_id: User
    payment_type: int
    provider: int
    account_no: int
    expiry: int


Product.update_forward_refs()
PaymentDetails.update_forward_refs()
OrderItems.update_forward_refs()
CartItem.update_forward_refs()

# class Payments(Document):
#     items: List[Items]
#     payer: Payer
#     back_urls: BackUrls
#     auto_return: AutoReturn
#     payment_methods: PaymentMethods
#     notification_url: NotificationUrl
#     statment_descriptor: StatmentDescriptor
#     extrnal_reference: ExtrnalReference
#     expire: Expire
#     expiration_date_from: ExpirationDateFrom
#     expiration_date_to: ExpirationDateTo


# class SchemasPayments(Payments):
#     class Config():
#         orm_mode = True


# Items.update_forward_refs()
# Payer.update_forward_refs()
# BackUrls.update_forward_refs()
# AutoReturn.update_forward_refs()
# PaymentMethods.update_forward_refs()
# NotificationUrl.update_forward_refs()
# StatmentDescriptor.update_forward_refs()
# ExtrnalReference.update_forward_refs()
# Expire.update_forward_refs()
# ExpirationDateFrom.update_forward_refs()
# ExpirationDateTo.update_forward_refs()


# class AggregationResponseItem(BaseModel):
#     id: str = Field(None, alias="_id")
#     total: int
