from django.core.management import BaseCommand

from branchData.utils.AbstractUtil import AbstractUtil


class Command(BaseCommand):
    help = 'Load data from all delivery services'

    def handle(self, *args, **options):
        self.load_data_for_all_subclasses(AbstractUtil)
        self.stdout.write('All data loaded')

    def load_data_for_all_subclasses(self, cls):
        for subclass in cls.__subclasses__():
            self.stdout.write(f'Loading data for {subclass.__name__}')
            instance = subclass()
            instance.load_data()
            self.stdout.write(f'Data loaded for {subclass.__name__}')
            self.load_data_for_all_subclasses(subclass)
