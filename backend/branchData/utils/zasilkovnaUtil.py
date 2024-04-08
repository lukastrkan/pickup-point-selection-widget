import json

import requests
from branchData.utils.AbstractUtil import AbstractUtil
from deliveryWidget import settings


class ZasilkovnaUtil(AbstractUtil):
    def parse_opening_hours(self, row):
        opening_hours = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [], "saturday": [],
                         "sunday": []}

        for day, hours in row['openingHours']['regular'].items():
            if hours != '':
                for hour in hours.split(', '):
                    hour = hour.split('–')
                    opening_hours[day].append({'open': hour[0], 'close': hour[1]})
        return opening_hours

    def load_data(self):
        url = f'https://www.zasilkovna.cz/api/v6/{settings.ZASILKOVNA_API_KEY}/branch.json'
        r = requests.get(url).content

        data = json.loads(r)

        for key, row in data['data'].items():
            id = row['id']
            name = row['name']
            address = row['street']
            city = row['city']
            zip = row['zip']
            country = row['country']
            latitude = row['latitude']
            longitude = row['longitude']
            box = row['place'] == 'Z-BOX'
            opening_hours = self.parse_opening_hours(row)
            card = row['creditCardPayment'] == 'yes'
            wheelchair = row['wheelchairAccessible'] == 'yes'

            self.save_or_update_branch(id, name, address, city, country, zip, latitude, longitude, opening_hours, box, card, wheelchair)

    def get_branch_id(self):
        return 4
