from app.model.base_model import BaseModel, db, Base


class Product(Base, BaseModel):

    __tablename__ = 'product'
    __origin = db.Column('origin', db.String(length=16))
    __sku = db.Column('sku', db.String(length=16))
    __seller_id = db.Column('seller_id', db.String(length=36))
    __product_code = db.Column('product_code', db.String(length=64))
    __gtin = db.Column('gtin', db.String(length=14))
    __name = db.Column('name', db.String(length=128))
    __status = db.Column('status', db.String(length=64))
    __brand = db.Column('brand', db.String(length=128))
    __description = db.Column('description', db.Text())
    __free_shipping = db.Column('free_shipping', db.Boolean())
    __group_id = db.Column('group_id', db.String(length=16))
    __tax_information_id = db.Column('tax_information_id', db.String(length=36))
    __approved = db.Column('approved', db.Boolean())
    __rejection_reasons = db.Column('rejection_reasons', db.Text())
    __active = db.Column('active', db.Boolean())
    __part_number = db.Column('part_number', db.String(length=32))
    __in_campaign = db.Column('in_campaign', db.Boolean())
    __odin = db.Column('odin', db.String(length=64))
    __waiting_invoice = db.Column('waiting_invoice', db.Boolean())
    __controller_gtin_id = db.Column('controller_gtin_id', db.String(length=36))
    __currency = db.Column('currency', db.String(length=3))
    __offer = db.Column('offer', db.Numeric())
    __price = db.Column('price', db.Numeric())
    __inactive_reason = db.Column('inactive_reason', db.String(length=64))

    def __init__(self):
        super().__init__()
