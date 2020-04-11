from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'create Site instance to store a domain name and display name for the current environment.'

    def add_arguments(self, parser):
        parser.add_argument('domain_name', type=str)
        parser.add_argument('display_name', type=str)

    def handle(self, *args, **options):
        domain_name = options['domain_name']
        display_name = options['display_name']

        try:
            site = Site.objects.create(domain=domain_name, name=display_name)
        except Exception as e:
            raise CommandError(e)

        self.stdout.write(self.style.SUCCESS(
            f"Site instance created with Domain Name = {site.domain} and Display Name = {site.name}"))
