from app.dao.base_dao import BaseDao
from app.model.product import Product


class ProductDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product'
        super().__init__(Product)

    def read(self, id: str = ''):
        return super().read(id)

    def create(self, model: Product) -> Product:
        return super().insert(model)

    def update(self, model: Product) -> Product:
        return super().update(model)

    def delete(self, id) -> dict:
        return super().delete(id)
