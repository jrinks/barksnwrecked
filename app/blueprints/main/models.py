from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(260), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    
    def __init__(self, username, email, password, phone):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.phone = phone
        
    def __repr__(self):
        return f'<User | {self.username}>'

class Category(db.Model):
    __table_args__ = {'extend_existing': True} 
    categoryid = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime)
    
    def __repr__(self):
        return f"Category('{self.categoryid}', '{self.category_name}')"

class Product(db.Model):
    productid = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(50), nullable = False)
    product_name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric)
    
    def __repr__(self):
        return f"Product('{self.productid}','{self.product_name}', '{self.description}', '{self.image}', '{self.quantity}', '{self.price}')"
# class ProductCategory(db.Model):
#     category_id = db.Column(db.Integer, db.ForeignKey('category.categoryid)'), nullable=False, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
#     created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # def __repr__(self):
    #     return f"Product('{self.category_id}', '{self.product_id}')"
    
class Cart(db.Model):
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable=False, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.productid'), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Product('{self.userid}','{self.product_id}','{self.quantity}')"
    
class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Numeric, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable=False, primary_key=True)
    
    def __repr__(self):
        return f"Order('{self.order_id}', '{self.order_date}', '{self.total_price}', '{self.userid}')"
    
class OrderedProduct(db.Model):
    orderproduct_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"OrderedProduct('{self.orderproduct_id}', '{self.order_id}', '{self.product_id}', '{self.quantity}')"
    
class SaleTransaction(db.Model):
    transactionid = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.order_id"), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
    cc_number = db.Column(db.String(50), nullable=False)
    cc_type = db.Column(db.String(50), nullable=False)
    response = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f"SaleTransaction('{self.transactionid}', '{self.order_id}', '{self.transaction_date}', '{self.amount}', '{self.cc_number}', '{self.cc_type}', '{self.response}')"