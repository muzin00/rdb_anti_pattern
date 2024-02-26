from django.db import models


class ConsumptionTax(models.Model):
    """
    消費税
    """

    class TaxRate(models.IntegerChoices):
        _005 = 0.05
        _008 = 0.08

    tax_rate = models.IntegerField(choices=TaxRate.choices, verbose_name="消費税率")
    activation_date = models.DateField(verbose_name="有効日")
    expiration_date = models.DateField(verbose_name="失効日")


class Sales(models.Model):
    """
    売上
    """

    class DeliveryStatus(models.TextChoices):
        ORDERING = "ORDERING", "発注中"
        DELIVERED = "DELIVERED", "発送済み"

    amount = models.PositiveIntegerField(verbose_name="売上金額")
    sales_date = models.DateTimeField(auto_now_add=True, verbose_name="売上日")
    delivery_status = models.CharField(
        default=DeliveryStatus.ORDERING,
        choices=DeliveryStatus.choices,
        verbose_name="配送状態",
    )

    class Meta:
        db_table = "sales"


class Product(models.Model):
    """
    商品
    """

    name = models.TextField(verbose_name="商品名")
    price = models.PositiveIntegerField(verbose_name="価格")

    class Meta:
        db_table = "products"


class Cart(models.Model):
    """
    カート
    """

    RELATED_NAME = "carts"

    sales = models.ForeignKey(
        Sales, on_delete=models.CASCADE, related_name=RELATED_NAME
    )
    products = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name=RELATED_NAME
    )
    quantity = models.PositiveIntegerField(verbose_name="数量")
    buyer = models.CharField(max_length=255, verbose_name="購入者")

    class Meta:
        db_table = "carts"
