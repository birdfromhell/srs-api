from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from collections import defaultdict
import models
import schemas
import database
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Read-only Restaurant API")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User endpoints
@app.get("/users", response_model=List[schemas.UserBase])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.get("/users/{user_id}", response_model=schemas.UserBase)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Image endpoints
@app.get("/images", response_model=List[schemas.ImageBase])
def get_images(db: Session = Depends(get_db)):
    images = db.query(models.Image).all()
    return images

@app.get("/images/{image_id}", response_model=schemas.ImageBase)
def get_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image

# Menu Category endpoints
@app.get("/menu-categories", response_model=List[schemas.MenuCategoryBase])
def get_menu_categories(db: Session = Depends(get_db)):
    categories = db.query(models.MenuCategory).all()
    return categories

@app.get("/menu-categories/{category_id}", response_model=schemas.MenuCategoryBase)
def get_menu_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.MenuCategory).filter(models.MenuCategory.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Menu category not found")
    return category

# Menu Item endpoints
@app.get("/menu-items", response_model=List[schemas.MenuItemBase])
def get_menu_items(db: Session = Depends(get_db)):
    items = db.query(models.MenuItem).all()
    return items

@app.get("/menu-items/{item_id}", response_model=schemas.MenuItemBase)
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

# FAQ Category endpoints
@app.get("/faqs", response_model=List[schemas.FAQCategoryResponse])
def get_faqs(db: Session = Depends(get_db)):
    query = select(models.FAQ, models.CategoryFaq).join(
        models.CategoryFaq,
        models.FAQ.category_id == models.CategoryFaq.id
    )
    results = db.execute(query).all()
    
    grouped_faqs = defaultdict(list)
    for faq, category in results:
        grouped_faqs[category.name].append({
            "title": faq.title,
            "text": faq.text
        })
    
    response = [
        {
            "name": category_name,
            "items": items
        }
        for category_name, items in grouped_faqs.items()
    ]
    
    return response

# Review endpoints
@app.get("/reviews", response_model=List[schemas.ReviewBase])
def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(models.Review).all()
    return reviews

@app.get("/reviews/{review_id}", response_model=schemas.ReviewBase)
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
