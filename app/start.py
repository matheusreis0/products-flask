from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from app.controller.product_controller import ProductController

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

api.add_resource(ProductController, '/api/product/', '/api/product/<uuid>', endpoint='products')

app.run(debug=True)
