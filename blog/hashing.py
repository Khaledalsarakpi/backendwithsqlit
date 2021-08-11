
from passlib.context import CryptContext
pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")



class Hash():

   def gethashing(string):
    return pwd_cxt.hash(string)

   def verify(hased_password,plain_password):
       return pwd_cxt.verify(plain_password,hased_password)


