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

    def __init__(self, origin: str = '', sku: str = '', seller_id: str = '', product_code: str = '', gtin: str = ''
                 , name: str = '', status: str = '', brand: str = '', description: str = '', free_shipping: bool = False
                 , group_id: str = '', tax_information_id: str = '', approved: bool = '', rejection_reasons: str = ''
                 , active: bool = False, part_number: str = '', in_campaign: bool = False, odin: str = ''
                 , waiting_invoice: bool = '', controller_gtin_id: str = '', currency: str = '', offer: float = 0.0
                 , price: float = 0.0):
        self.__origin = origin
        self.__sku = sku
        self.__seller_id = seller_id
        self.__product_code = product_code
        self.__gtin = gtin
        self.__name = name
        self.__status = status
        self.__brand = brand
        self.__description = description
        self.__free_shipping = free_shipping
        self.__group_id = group_id
        self.__tax_information_id = tax_information_id
        self.__approved = approved
        self.__rejection_reasons = rejection_reasons
        self.__active = active
        self.__part_number = part_number
        self.__in_campaign = in_campaign
        self.__odin = odin
        self.__waiting_invoice = waiting_invoice
        self.__controller_gtin_id = controller_gtin_id
        self.__currency = currency
        self.__offer = offer
        self.__price = price

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'origin': self.origin,
            'sku': self.sku,
            'seller_id': self.seller_id,
            'product_code': self.product_code,
            'gtin': self.gtin,
            'name': self.name,
            'status': self.status,
            'brand': self.brand,
            'description': self.description,
            'free_shipping': self.free_shipping,
            'group_id': self.group_id,
            'tax_information_id': self.tax_information_id,
            'approved': self.approved,
            'rejection_reasons': self.rejection_reasons,
            'active': self.active,
            'part_number': self.part_number,
            'in_campaign': self.in_campaign,
            'odin': self.odin,
            'waiting_invoice': self.waiting_invoice,
            'controller_gtin_id': self.controller_gtin_id,
            'currency': self.currency,
            'offer': self.offer,
            'price': self.price,
        }

    @property
    def origin(self) -> str:
        return str(self.__origin)

    @origin.setter
    def origin(self, origin: str):
        self.__origin = origin

    @property
    def sku(self) -> str:
        return str(self.__sku)

    @sku.setter
    def sku(self, sku: str):
        self.__sku = sku

    @property
    def seller_id(self) -> str:
        return str(self.__seller_id)

    @seller_id.setter
    def seller_id(self, seller_id: str):
        self.__seller_id = seller_id

    @property
    def product_code(self) -> str:
        return str(self.__product_code)

    @product_code.setter
    def product_code(self, product_code: str):
        self.__product_code = product_code

    @property
    def gtin(self) -> str:
        return str(self.__gtin)

    @gtin.setter
    def gtin(self, gtin: str):
        self.__gtin = gtin

    @property
    def name(self) -> str:
        return str(self.__name)

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def status(self) -> str:
        return str(self.__status)

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def brand(self) -> str:
        return str(self.__brand)

    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def description(self) -> str:
        return str(self.__description)

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def free_shipping(self) -> bool:
        return bool(self.__free_shipping)

    @free_shipping.setter
    def free_shipping(self, free_shipping: bool):
        self.__free_shipping = free_shipping

    @property
    def group_id(self) -> str:
        return str(self.__group_id)

    @group_id.setter
    def group_id(self, group_id: str):
        self.__group_id = group_id

    @property
    def tax_information_id(self) -> str:
        return str(self.__tax_information_id)

    @tax_information_id.setter
    def tax_information_id(self, tax_information_id: str):
        self.__tax_information_id = tax_information_id

    @property
    def approved(self) -> bool:
        return bool(self.__approved)

    @approved.setter
    def approved(self, approved: bool):
        self.__approved = approved

    @property
    def rejection_reasons(self) -> str:
        return str(self.__rejection_reasons)

    @rejection_reasons.setter
    def rejection_reasons(self, rejection_reasons: str):
        self.__rejection_reasons = rejection_reasons

    @property
    def active(self) -> bool:
        return bool(self.__active)

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def part_number(self) -> str:
        return str(self.__part_number)

    @part_number.setter
    def part_number(self, part_number: str):
        self.__part_number = part_number

    @property
    def in_campaign(self) -> bool:
        return bool(self.__in_campaign)

    @in_campaign.setter
    def in_campaign(self, in_campaign: bool):
        self.__in_campaign = in_campaign

    @property
    def odin(self) -> str:
        return str(self.__odin)

    @odin.setter
    def odin(self, odin: str):
        self.__odin = odin

    @property
    def waiting_invoice(self) -> bool:
        return bool(self.__waiting_invoice)

    @waiting_invoice.setter
    def waiting_invoice(self, waiting_invoice: bool):
        self.__waiting_invoice = waiting_invoice

    @property
    def controller_gtin_id(self) -> str:
        return str(self.__controller_gtin_id)

    @controller_gtin_id.setter
    def controller_gtin_id(self, controller_gtin_id: str):
        self.__controller_gtin_id = controller_gtin_id

    @property
    def currency(self) -> str:
        return str(self.__currency)

    @currency.setter
    def currency(self, currency: str):
        self.__currency = currency

    @property
    def offer(self) -> float:
        return float(self.__offer)

    @offer.setter
    def offer(self, offer: float):
        self.__offer = offer

    @property
    def price(self) -> float:
        return float(self.__price)

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def inactive_reason(self) -> str:
        return str(self.__inactive_reason)

    @inactive_reason.setter
    def inactive_reason(self, inactive_reason: str):
        self.__inactive_reason = inactive_reason
