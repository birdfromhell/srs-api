from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: str
    username: str

    class Config:
        from_attributes = True

class ImageBase(BaseModel):
    image_url: str
    orientation: str
    created_at: datetime

    class Config:
        from_attributes = True

class MenuCategoryBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None

    class Config:
        from_attributes = True

class MenuItemBase(BaseModel):
    title: str
    price: float
    currency: Optional[str] = None
    rating: Optional[int] = None
    text: Optional[str] = None
    image_url: Optional[str] = None
    badge: Optional[str] = None
    category_id: int

    class Config:
        from_attributes = True

class FAQCategoryBase(BaseModel):
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class FAQBase(BaseModel):
    title: str
    text: str
    category_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ReviewBase(BaseModel):
    title: str
    name: str
    rating: int
    image: str
    text: str

    class Config:
        from_attributes = True
