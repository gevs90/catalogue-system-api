from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    name: str
    email: str
    password: str
    role: str


class UserSchema(BaseModel):
    name: str
    email: str
    password: str | None = None


class EmailSchema(BaseModel):
    email: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
