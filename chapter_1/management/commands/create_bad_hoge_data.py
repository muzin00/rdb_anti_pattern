from django.core.management.base import BaseCommand

from chapter_1.models import BadHoge


class Command(BaseCommand):
    help = "Create bad hoge data"

    def handle(self, *args, **options):
        BadHoge.objects.bulk_create(
            [
                BadHoge(delete_falg=1),
                BadHoge(delete_falg=2),
                BadHoge(delete_falg=0),
                BadHoge(delete_falg=9),
                BadHoge(delete_falg=99),
                BadHoge(delete_falg=None),
            ]
        )
