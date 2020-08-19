from app.dao.product_dao import ProductDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product import Product


class ProductController(Resource):

    def __init__(self):
        self.__dao = ProductDao()

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
