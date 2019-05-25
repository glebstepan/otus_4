from flask import Flask, request, render_template, Blueprint

from products_list import products

products_app = Blueprint('products_app', __name__)



@products_app.route('/', endpoint='products')
def products_page():
    response = render_template(
        'products.html',
        products=products
    )
    return response

@products_app.route('/<int:product_id>/', endpoint='product')
def product_page(product_id):
    response = render_template(
        'product.html',
        product=products[product_id]
    )
    return response
