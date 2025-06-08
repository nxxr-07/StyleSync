# StyleSync E-commerce Web App

StyleSync is a modern, student-built e-commerce web application for fashion shopping, featuring user authentication, product catalog, cart, order management, admin panel, and an AI stylist tool. Built with Flask and SQLAlchemy, it offers a seamless shopping experience with a stylish UI.

## Features

- **User Authentication:** Sign up, sign in, and secure session management.
- **Product Catalog:** Browse products with filters for category, price, and color.
- **Shopping Cart:** Add, remove, and update product quantities in your cart.
- **Order Management:** Place orders and view your order history.
- **Admin Panel:** Manage products, view users, and see all sales/orders.
- **Contact Form:** Users can send messages to the site admins.
- **AI Stylist:** Get outfit recommendations and color matching tips.
- **Responsive Design:** Works well on desktop and mobile devices.

## Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Database:** SQLite (default, via SQLAlchemy)
- **Templating:** Jinja2

## Project Structure

```
.
├── app.py                  # Main Flask app and routes
├── auth.py                 # Authentication blueprint
├── config.py               # App configuration
├── create_missing_tables.py# Script to create DB tables
├── database.py             # (Duplicate of create_missing_tables.py)
├── models.py               # SQLAlchemy models
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   └── js/
│       └── script.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── shop.html
│   ├── cart.html
│   ├── signin.html
│   ├── signup.html
│   ├── admin.html
│   ├── admin_sales.html
│   ├── orders.html
│   ├── about.html
│   ├── blog.html
│   ├── contact.html
│   ├── sproduct.html
│   └── ai_stylist.html
└── instance/
    └── site.db             # SQLite database (auto-created)
```

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd finalYearFlaskProject
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Initialize the Database

```sh
python create_missing_tables.py
```

This will create `instance/site.db` with all required tables.

### 5. Run the Application

```sh
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Admin Login

- **Email:** `admin@ss`
- **Password:** `admin@ss`

Admin can add/remove products, view users, and see all orders.

## Customization

- **Add Products:** Use the admin panel or insert directly into the database.
- **Images:** Place product images in `static/images/products/`.
- **Styling:** Modify `static/css/style.css` for custom styles.

## Notes

- The project uses SQLite for simplicity. For production, switch to PostgreSQL or MySQL in `config.py`.
- Secret keys and credentials should be managed securely in production.

## License

This project is for educational purposes.

---

**Made with ❤️ by the StyleSync Team**