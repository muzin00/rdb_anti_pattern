from django.db import models


class BadHoge(models.Model):
    delete_falg = models.IntegerField(default=0, null=True, verbose_name="削除フラグ")

    class Meta:
        db_table = "bad_hoge"


class GoodHoge(models.Model):
    is_deleted = models.BooleanField(default=False, verbose_name="削除フラグ")

    class Meta:
        db_table = "good_hoge"
