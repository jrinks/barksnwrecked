from . import bp as main
from flask_session import Session
from flask import Flask, render_template, redirect, request, session
from .models import Product, Category, Cart, Order, SaleTransaction
from app.blueprints.auth.models import User

@main.route('/', methods=['GET'])
@main.route('/home')
def home():
    return render_template('index.html')
    items = db.execute("SELECT * FROM products ORDER BY name")
    itemsLen = len(items)
    shopping_cart = []
    shopLen = len(shopping_cart)
    totItems, total, display = 0, 0, 0
    if User in session:
        shopping_cart = db.execute("SELECT product_name, image, quantity, price FROM products")
        shopLen=len(shopping_cart)
        for i in range(shopLen):
            total += shoppingCart[i]["SUM(price)"]
            totItems += shoppingCart[i]["SUM(quantity)"]
        items = db.execute("SELECT * FROM products ORDER BY name")
    return render_template('/templates/cart.html', **context, home=home)
    
        
@main.route('/productDescription')
def productDescrption():
    pass
@main.route("/addtoCart")
def addtoCart():
    pass
@main.route("/cart")
def cart():
    if User in session:
        totItems, total, display = 0,0,0
        shoppingCart = db.execute("SELECT product_name, image, quantity, price From products")
        shopLen = len(shoppingCart)
        for i in range(shopLen):
            total += shoppingCart[i]["SUM(total"]
    return render_template('cart.html', **context, home=home)
@main.route('/category')
def category():
    pass
@main.route('/products')
def product(product_id):
    pass
@main.route('/users')
def getUsers():
    pass
@main.route('/removefromCart')
def removeFromCart():
    pass
@main.route('/checkoutPage')
def checkoutForm():
    pass
@main.route('/createorder', methods=['GET', 'POST'])
def createOrder():
    pass