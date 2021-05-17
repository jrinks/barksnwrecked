from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

def valid_login(email, password):
    current = mysql.connection.cursor()
    current.execute("Select email, password from User")
    userData = current.fetchall()
    current.close
class CategoryForm(FlaskForm):
    pass

class ProductForm(FlaskForm):
    def getAllProducts():
        itemdata= Product.query.join(ProductCateogory, Product.productid == ProductCategory.productid) \ 
            .add_columns(Product.productid, Product.product_name, Product.discounted_price, Product.description, Product.image, Product.quantity) \
            .join(Category, Category.categoryid == ProductCategory.categoryid) \
            .order_by(Category.categoryid.desc())
            .all()
    return itemdata 

class checkoutForm(FlaskForm):
    pass