# from app.dao.base_dao import BaseDao
# from app.model.product import Product


class ProductDao:

    def __init__(self):
        self.__table_name = 'product'
        super().__init__()

    def read(self, id: str = ''):
        return super().read(id)

    def create(self, model):
        model.id = super().insert()
        return model

    def update(self, model):
        return super().update(model)

    def delete(self, id):
        return super().delete(id)
