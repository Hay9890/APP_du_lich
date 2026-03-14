from pydantic import BaseModel, EmailStr


class AdminLogin(BaseModel):
    email: EmailStr
    password: str


class AdminResponse(BaseModel):
    id: str
    email: EmailStr
    role: str
    access_token: str
    token_type: str = "bearer"
