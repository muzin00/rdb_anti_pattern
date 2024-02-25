from django.db import models


class BadHoge(models.Model):
    delete_falg = models.IntegerField(default=0, null=True, verbose_name="削除フラグ")

    class Meta:
        db_table = "bad_hoge"
