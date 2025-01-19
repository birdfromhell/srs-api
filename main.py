from flask import Flask, jsonify, abort
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from collections import defaultdict
import models
import schemas
import database
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User endpoints
@app.route("/users", methods=["GET"])
def get_users():
    db = next(get_db())
    users = db.query(models.User).all()
    return jsonify([schemas.UserBase.from_orm(user).dict() for user in users])

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    db = next(get_db())
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        abort(404, description="User not found")
    return jsonify(schemas.UserBase.from_orm(user).dict())

# Image endpoints
@app.route("/images", methods=["GET"])
def get_images():
    db = next(get_db())
    images = db.query(models.Image).all()
    return jsonify([schemas.ImageBase.from_orm(image).dict() for image in images])

@app.route("/images/<int:image_id>", methods=["GET"])
def get_image(image_id: int):
    db = next(get_db())
    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if not image:
        abort(404, description="Image not found")
    return jsonify(schemas.ImageBase.from_orm(image).dict())

# Menu Category endpoints
@app.route("/menu-categories", methods=["GET"])
def get_menu_categories():
    db = next(get_db())
    categories = db.query(models.MenuCategory).all()
    return jsonify([schemas.MenuCategoryBase.from_orm(category).dict() for category in categories])

@app.route("/menu-categories/<int:category_id>", methods=["GET"])
def get_menu_category(category_id: int):
    db = next(get_db())
    category = db.query(models.MenuCategory).filter(models.MenuCategory.id == category_id).first()
    if not category:
        abort(404, description="Menu category not found")
    return jsonify(schemas.MenuCategoryBase.from_orm(category).dict())

# Menu Item endpoints
@app.route("/menu-items", methods=["GET"])
def get_menu_items():
    db = next(get_db())
    items = db.query(models.MenuItem).all()
    return jsonify([schemas.MenuItemBase.from_orm(item).dict() for item in items])

@app.route("/menu-items/<int:item_id>", methods=["GET"])
def get_menu_item(item_id: int):
    db = next(get_db())
    item = db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()
    if not item:
        abort(404, description="Menu item not found")
    return jsonify(schemas.MenuItemBase.from_orm(item).dict())

# FAQ Category endpoints
@app.route("/faqs", methods=["GET"])
def get_faqs():
    db = next(get_db())
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
    
    return jsonify(response)

# Review endpoints
@app.route("/reviews", methods=["GET"])
def get_reviews():
    db = next(get_db())
    reviews = db.query(models.Review).all()
    return jsonify([schemas.ReviewBase.from_orm(review).dict() for review in reviews])

@app.route("/reviews/<int:review_id>", methods=["GET"])
def get_review(review_id: int):
    db = next(get_db())
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        abort(404, description="Review not found")
    return jsonify(schemas.ReviewBase.from_orm(review).dict())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
