from flask import Blueprint, session, request
from flask import render_template


products_app = Blueprint('products-app', __name__)


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


@products_app.route('/')
def products_page():
    return '<h1>will be redirect</h1>'


@products_app.route('/<name>')
def product_page(name):
    for item in products:
        if item.name == name:
            product = item
            break
    response = render_template(
        'product.html',
        product = product
    )
    return response


