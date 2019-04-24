from django.core.management.base import BaseCommand
from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ShopUser.objects.filter(shopuserprofile__isnull=True)
        for user in users:
            users_profile = ShopUserProfile.objects.create(user=user)
