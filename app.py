from flask import Flask, render_template,  redirect, url_for, session
from flask import request, flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Product
from auth import auth_bp
from functools import wraps

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.secret_key = 'your_secret_key_'

app.register_blueprint(auth_bp)

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.signin'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_admin'):
            flash('Admin access required!')
            return redirect(url_for('auth.signin'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    products = Product.query.all()
    new_products = Product.query.order_by(Product.id.desc()).limit(8).all()
    return render_template('index.html', products=products, new_products=new_products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/cart')
@login_required
def cart():
    cart = session.get('cart', {})
    cart_items = []
    subtotal = 0

    for product_id, quantity in cart.items():
        try:
            pid = int(product_id)
        except ValueError:
           
            continue  # skip invalid keys
        product = Product.query.get(pid)
        if product:
            item_total = product.price * quantity
            subtotal += item_total
            cart_items.append({
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'price': product.price,
                'quantity': quantity,
                'total': item_total
            })

    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal, total=subtotal)

@app.route('/reset_cart', methods=['POST'])
def reset_cart():
    session.pop('cart', None)
    return redirect(url_for('home'))

@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:product_id>')
@login_required
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    cart.pop(str(product_id), None)
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)

@app.route('/sproduct')
def sproduct():
    return render_template('sproduct.html')

@app.route('/ai')
def ai():
    return render_template('ai_stylist.html')

@app.route('/admin', methods=['GET'])
@admin_required
def admin_panel():
    products = Product.query.all()
    users = User.query.all()
    return render_template('admin.html', products=products, users=users)

@app.route('/admin/add_product', methods=['POST'])
@admin_required
def admin_add_product():
    name = request.form['name']
    brand = request.form['brand']
    price = request.form['price']
    image = request.form['image']
    product = Product(name=name, brand=brand, price=price, image=image)
    db.session.add(product)
    db.session.commit()
    flash('Product added!')
    return redirect(url_for('admin_panel'))

@app.route('/admin/remove_product', methods=['POST'])
@admin_required
def admin_remove_product():
    product_id = request.form['product_id']
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('Product removed!')
    else:
        flash('Product not found!')
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    app.run(debug=True)
