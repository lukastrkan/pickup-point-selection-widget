from abc import ABC, abstractmethod

from branchData.models import Branch, BranchType


class AbstractUtil(ABC):
    branch_type = None

    def __init__(self):
        self.branch_type = BranchType.objects.get(pk=self.get_branch_id())

    @abstractmethod
    def parse_opening_hours(self, row):
        raise NotImplementedError

    @abstractmethod
    def load_data(self):
        raise NotImplementedError

    @abstractmethod
    def get_branch_id(self):
        raise NotImplementedError

    def save_or_update_branch(self, branch_id, name, address, city, country, zip, latitude, longitude, opening_hours,
                              box, card=False, wheelchair=False):
        obj = Branch.objects.get_or_create(branchId=branch_id, branch_type=self.branch_type,
                                           defaults={'name': name, 'address': address, 'city': city, 'zip': zip,
                                                     'country': country, 'latitude': latitude, 'longitude': longitude,
                                                     'openning_hours': opening_hours, 'box': box, 'card': card, 'wheelchair': wheelchair})

        if not obj[1]:
            obj = obj[0]
            obj.name = name
            obj.address = address
            obj.city = city
            obj.zip = zip
            obj.country = country
            obj.latitude = latitude
            obj.longitude = longitude
            obj.openning_hours = opening_hours
            obj.box = box
            obj.card = card
            obj.wheelchair = wheelchair
            obj.save()
