from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    id: str = Field(..., max_length=45, example="user123")
    name: str = Field(..., max_length=45, example="John Doe")
    password: str = Field(..., min_length=6, example="securepassword")


# 사용자 응답용 모델
class UserOut(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True
