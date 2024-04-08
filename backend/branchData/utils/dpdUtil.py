import requests
import xml.etree.ElementTree as ET

from branchData.utils.AbstractUtil import AbstractUtil


class DpdUtil(AbstractUtil):
    day_map = {
        '1': 'monday',
        '2': 'tuesday',
        '3': 'wednesday',
        '4': 'thursday',
        '5': 'friday',
        '6': 'saturday',
        '7': 'sunday',
    }

    def load_data(self):
        url = 'https://pickup.dpd.cz/export/xml?country=203'
        r = requests.get(url).content

        root = ET.fromstring(r)

        for row in root.findall('.//parcelshop'):
            id = row.find('id').text
            name = row.find('company').text
            address = row.find('street').text
            house_number = row.find('house_number').text
            if house_number:
                address += ' ' + house_number
            city = row.find('city').text
            zip = row.find('postcode').text
            country = 'cz'
            latitude = row.find('latitude').text
            longitude = row.find('longitude').text
            box = row.find('pickup_network_type').text == 'dpd_box'
            opening_hours = self.parse_opening_hours(row)
            card = row.find('cardpayment_allowed').text == '1'

            self.save_or_update_branch(id, name, address, city, country, zip, latitude, longitude, opening_hours, box,
                                       card)
        pass

    def get_branch_id(self):
        return 6

    def parse_opening_hours(self, row):
        opening_hours = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [], "saturday": [],
                         "sunday": []}
        for dayEl in row.find('opening_hours').findall('opening'):
            day = dayEl.find('day').attrib['day']
            current_day = self.day_map[day]
            open_morning = dayEl.find('openMorning').text
            close_morning = dayEl.find('closeMorning').text

            if open_morning and close_morning:
                opening_hours[current_day].append({'open': open_morning, 'close': close_morning})

            open_afternoon = dayEl.find('openAfternoon').text
            close_afternoon = dayEl.find('closeAfternoon').text

            if open_afternoon and close_afternoon:
                opening_hours[current_day].append({'open': open_afternoon, 'close': close_afternoon})
        return opening_hours
