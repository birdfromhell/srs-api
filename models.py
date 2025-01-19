from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    username = Column(String(100), unique=True)
    
    images = relationship('Image', back_populates='user')

class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(500), nullable=False)
    orientation = Column(String(1), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='images')

    def to_dict(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'orientation': self.orientation,
            'created_at': self.created_at.isoformat()
        }

class MenuCategory(Base):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    description = Column(Text)

    menu_items = relationship('MenuItem', back_populates='category')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'description': self.description
        }

class MenuItem(Base):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(String(10))
    rating = Column(Integer)
    text = Column(Text)
    image_url = Column(String(500))
    badge = Column(String(200))
    category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    
    category = relationship('MenuCategory', back_populates='menu_items')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'currency': self.currency,
            'rating': self.rating,
            'text': self.text,
            'image_url': self.image_url,
            'badge': self.badge,
            'category_id': self.category_id
        }


class CategoryFaq(Base):
    __tablename__ = 'category_faq'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    faqs = relationship('FAQ', back_populates='category', cascade="all, delete-orphan")

class FAQ(Base):
    __tablename__ = 'faq'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    text = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey('category_faq.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    category = relationship('CategoryFaq', back_populates='faqs')

class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    name = Column(String(50), nullable=False)
    rating = Column(Integer, nullable=False)
    image = Column(String(100), nullable=False)
    text = Column(Text, nullable=False)
