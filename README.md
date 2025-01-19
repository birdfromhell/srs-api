# srs-api

This project is a REST API built using Flask.

## Requirements

- Python 3.7+
- Flask
- SQLAlchemy
- PyMySQL

## Installation

1. Clone the repository:

```bash
git clone https://github.com/birdfromhell/srs-api.git
cd srs-api
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database:

Make sure to configure your database settings in the `.env` file.

## Running the API

To run the API, use the following command:

```bash
python main.py
```

The API will be available at `http://localhost:8000`.

## Endpoints

### Users

- `GET /users`: Get a list of all users.
- `GET /users/{user_id}`: Get details of a specific user.

### Images

- `GET /images`: Get a list of all images.
- `GET /images/{image_id}`: Get details of a specific image.

### Menu Categories

- `GET /menu-categories`: Get a list of all menu categories.
- `GET /menu-categories/{category_id}`: Get details of a specific menu category.

### Menu Items

- `GET /menu-items`: Get a list of all menu items.
- `GET /menu-items/{item_id}`: Get details of a specific menu item.

### FAQs

- `GET /faqs`: Get a list of all FAQs grouped by category.

### Reviews

- `GET /reviews`: Get a list of all reviews.
- `GET /reviews/{review_id}`: Get details of a specific review.
