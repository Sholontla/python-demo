from passlib.context import CryptContext

crypto_pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
class HashAuthentication:
    def bcryptHasshing(password: str):
        hashedPassword = crypto_pwd.hash(password)
        return hashedPassword

    def verify(hashed_password, plain_password):
        return crypto_pwd.verify(plain_password, hashed_password)