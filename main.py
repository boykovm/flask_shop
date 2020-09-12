from flask import Flask, request, render_template, session

from product_view import products_app


app = Flask(__name__)
app.register_blueprint(products_app, url_prefix='/products/')


class Products:
    def __init__(self, name, price, spec, img):
        self.name = name
        self.price = price
        self.spec = spec
        self.img = img

products = {
            Products('iMac silver', 999, 'iMac silver iMac silver iMac silver', 'mac1.jpg'),
            Products('iMac black', 888, 'iMac black iMac black iMac black', 'mac2.jpg'),
            Products('iMac rose', 777, 'iMac rose iMac rose iMac rose', 'mac3.jpg')
}


@app.route('/')
def index_page(name = 'Products'):
    response = render_template(
        'index.html',
        name=name,
        products=products

    )
    return response


app.run(host='localhost', port=8000, debug=True)