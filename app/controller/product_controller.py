from app.dao.product_dao import ProductDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product import Product


class ProductController(Resource):

    def __init__(self):
        self.__dao = ProductDao()

    def get(self, uuid=None):
        if uuid:
            model = self.__dao.read(uuid)
            if model:
                return jsonify(model.to_dict())
            return {}
        return jsonify([product.to_dict() for product in self.__dao.read()])

    def post(self):
        data = request.get_json()
        product = Product(**data)
        model = self.__dao.create(product)
        return self.verify_sql_error(model)

    def put(self, uuid):
        data = request.get_json()
        product = Product(**data)
        product.id = uuid
        model = self.__dao.update(product)
        return self.verify_sql_error(model)

    def delete(self, uuid=None):
        message = self.__dao.delete(uuid)
        return jsonify(message)

    def verify_sql_error(self, m):
        if type(m) == Product:
            return jsonify(m.to_dict())
        return jsonify(m)
