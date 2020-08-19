from app.dao.product_dao import ProductDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product import Product


class ProductController(Resource):

    def __init__(self):
        self.__dao = ProductDao()

    def get(self, uuid=None):
        if uuid:
            return jsonify(self.__dao.read(uuid).to_dict())
        return jsonify([product.to_dict() for product in self.__dao.read()])

    def post(self):
        data = request.get_json()
        product = Product(**data)
        model = self.__dao.create(product)
        return jsonify(model.to_dict())

    def put(self, uuid):
        data = request.get_json()
        product = Product(**data)
        product.id = uuid
        model = self.__dao.update(product)
        return jsonify(model.to_dict())

    def delete(self, uuid=None):
        return jsonify(self.__dao.delete(uuid))
