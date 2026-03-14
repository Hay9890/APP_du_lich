from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=1, max_length=72)


class UserInDB(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    role: str = "user"


class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr