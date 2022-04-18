
from typing import Optional, List
from pydantic import BaseModel
from beanie import Document, Indexed, init_beanie
import asyncio, motor
from testings.schemastest import Payments
async def post():
    # Beanie uses Motor under the hood 
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongoadmin:mongoadmin@localhost:27017")

    # Init beanie with the Product document class
    await init_beanie(database=client.db_name, document_models=[Payments])

    # Beanie documents work just like pydantic models
    payment = Payments()
    # And can be inserted into the database
    await payment.insert() 

    # You can find documents with pythonic syntax
    payment = await Payments.find_one(Payments.items)
    # And update them
    #return await payment.set({Payment.name:"Gold bar"})







