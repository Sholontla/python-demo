from typing import Any, List, Dict, Optional, Tuple
from beanie.odm.documents import Document
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from pydantic import Field
from testings.config_data import curr, pro, items_structure
from pprint import pprint

# ---------------------------------------------------------------------------------------------
class Items(BaseModel):
    title: str
    currency_id: str
    picture_url: str
    description: str
    category_id: str
    quantity: str
    unit_price: str

class Payer(BaseModel):
    name: str
    surname: str
    email: str
    phone: dict
    idetnification: dict
    address: dict

class BackUrls(BaseModel):
    success: str
    failure: str
    pending: str

class AutoReturn(BaseModel):
    auto_return: str

class PaymentMethods(BaseModel):
    excluded_pyment_methods: dict
    excluded_pyment_types: dict
    installments: str

# class PaymenMethods(BaseModel):
#     excluded_pyment_methods: Dict[str, int]
#     excluded_pyment_types: Dict[str, int]
#     installments: str

class NotificationUrl(BaseModel): 
    notification_url: str

class StatmentDescriptor(BaseModel): 
    statment_descriptor: str

class ExtrnalReference(BaseModel): 
    extrnal_reference: str

class Expire(BaseModel): 
    expire: str

class ExpirationDateFrom(BaseModel): 
    expiration_date_from: str

class ExpirationDateTo(BaseModel): 
    expiration_date_to: str = Field()


class Payments(Document):
    items: List[Items]
    payer: Payer
    back_urls: BackUrls
    auto_return: AutoReturn
    payment_methods: PaymentMethods
    notification_url: NotificationUrl
    statment_descriptor: StatmentDescriptor
    extrnal_reference: ExtrnalReference
    expire: Expire
    expiration_date_from: ExpirationDateFrom
    expiration_date_to: ExpirationDateTo


class SchemasPayments(Payments):
    class Config():
        orm_mode = True


Items.update_forward_refs()
Payer.update_forward_refs()
BackUrls.update_forward_refs()
AutoReturn.update_forward_refs()
PaymentMethods.update_forward_refs()
NotificationUrl.update_forward_refs()
StatmentDescriptor.update_forward_refs()
ExtrnalReference.update_forward_refs()
Expire.update_forward_refs()
ExpirationDateFrom.update_forward_refs()
ExpirationDateTo.update_forward_refs()


class AggregationResponseItem(BaseModel):
    id: str = Field(None, alias="_id")
    total: int
