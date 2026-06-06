
from pydantic import BaseModel
class usercreate(BaseModel):
    name: str
    email: str
class userupdate(BaseModel):
    name: str
    email: str
class userdelete(BaseModel):
    pass