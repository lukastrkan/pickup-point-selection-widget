import requests

from branchData.utils.AbstractUtil import AbstractUtil
from deliveryWidget import settings

BALIKOBOT_USERNAME = settings.BALIKOBOT_USERNAME
BALIKOBOT_PASSWORD = settings.BALIKOBOT_PASSWORD


class BalikobotPPLUtil(AbstractUtil):
    def get_branch_id(self):
        return 7

    def load_data(self):
        response = requests.get('https://api.balikobot.cz/ppl/fullbranches/4/CZ',
                                auth=(BALIKOBOT_USERNAME, BALIKOBOT_PASSWORD)).json()
        for key, row in response['branches'].items():
            id = row['id']
            name = row['name']
            address = row['street']
            city = row['city']
            zip = row['zip']
            country = row['country']
            latitude = row['latitude']
            longitude = row['longitude']
            box = row['type'] == 'box'
            opening_hours = self.parse_opening_hours(row)

            self.save_or_update_branch(id, name, address, city, country, zip, latitude, longitude, opening_hours, box)
        pass

    def parse_opening_hours(self, row):
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        opening_hours = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [], "saturday": [],
                         "sunday": []}

        for day in days:
            current_day = row[f'opening_{day}']
            if current_day:
                current_day = current_day.split(',')
                for hour in current_day:
                    hour = hour.split('-')
                    opening_hours[day].append({'open': hour[0], 'close': hour[1]})
        return opening_hours
