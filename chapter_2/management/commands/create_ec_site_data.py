from datetime import date, datetime

from django.core.management.base import BaseCommand
from django.db import transaction

from chapter_2.models import Cart, ConsumptionTax, Product, Sales


class Command(BaseCommand):
    help = "Create ec site data"

    @transaction.atomic
    def handle(self, *args, **options):
        # 消費税
        consumption_tax_1 = ConsumptionTax.objects.create(
            tax_rate=1.05,
            activation_date=date(1997, 4, 1),
            expiration_date=date(2014, 3, 31),
        )
        consumption_tax_2 = ConsumptionTax.objects.create(
            tax_rate=1.08,
            activation_date=date(2014, 4, 1),
        )

        # 商品
        product_1 = Product.objects.create(name="SQL 実践入門", price=2580)
        product_2 = Product.objects.create(name="リーダブルコード", price=2592)
        product_3 = Product.objects.create(name="プログラマのためのSQL", price=4200)
        product_4 = Product.objects.create(name="データベース・リファクタリング", price=3000)

        # カート
        cart_1 = Cart(product=product_1, quantity=3, buyer="sone")
        cart_2 = Cart(product=product_2, quantity=3, buyer="sone")
        cart_3 = Cart(product=product_3, quantity=3, buyer="sone")

        # 売上
        sales = Sales.objects.create(
            amount=round(
                (cart_1.total_price() + cart_2.total_price() + cart_3.total_price())
                * consumption_tax_1.tax_rate
            ),
            sales_date=datetime(2014, 3, 21, 23, 59, 59),
            consumption_tax=consumption_tax_1,
        )
        sales.carts.add(cart_1, cart_2, cart_3, bulk=False)
