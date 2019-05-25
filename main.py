from flask import Flask, request, render_template

from products_views import products_app
from cart_views import cart_app


app = Flask(__name__)
app.register_blueprint(products_app, url_prefix='/products/')
app.register_blueprint(cart_app, url_prefix='/cart/')

@app.route('/')

def index_page():
    response = render_template(
        'index.html'
    )
    return response



if __name__ == "__main__":

    app.run('localhost', 8080, debug=True)
