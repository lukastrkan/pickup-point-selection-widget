import requests
from xml.etree import ElementTree as ET
from branchData.utils.AbstractUtil import AbstractUtil


class CeskaPostaUtil(AbstractUtil):
    def get_branch_id(self):
        return 1

    day_map = {
        'Pondělí': 'monday',
        'Úterý': 'tuesday',
        'Středa': 'wednesday',
        'Čtvrtek': 'thursday',
        'Pátek': 'friday',
        'Sobota': 'saturday',
        'Neděle': 'sunday',
    }
    ns = {'ns': 'http://www.cpost.cz/schema/aict/zv_1'}

    def download_data(self):
        url = 'http://napostu.ceskaposta.cz/vystupy/napostu_1.xml'
        r = requests.get(url).content
        root = ET.fromstring(r)
        return root

    def load_data(self):
        root = self.download_data()

        for row in root.findall('.//ns:row', self.ns):
            id = row.find('ns:PSC', self.ns).text
            name = row.find('ns:NAZ_PROV', self.ns).text
            address = row.find('ns:ADRESA', self.ns).text
            city = row.find('ns:OBEC', self.ns).text
            zip = row.find('ns:PSC', self.ns).text
            country = 'cz'
            latitude = row.find('ns:SOUR_Y_WGS84', self.ns).text
            longitude = row.find('ns:SOUR_X_WGS84', self.ns).text
            oppening_hours = self.parse_opening_hours(row)

            self.save_or_update_branch(id, name, address, city, country, zip, latitude, longitude, oppening_hours,
                                       False, True)

    def parse_opening_hours(self, row):
        opening_hours = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [], "saturday": [],
                         "sunday": []}
        for day in row.find('ns:OTV_DOBA', self.ns):
            current_day = self.day_map[day.attrib['name']]
            for op in day.findall('ns:od_do', self.ns):
                opening_hours[current_day].append(
                    {'open': op.find('ns:od', self.ns).text, 'close': op.find('ns:do', self.ns).text})
        return opening_hours


class BalikovnaUtil(CeskaPostaUtil):
    ns = {'ns': 'http://www.cpost.cz/schema/aict/zv_2'}

    def get_branch_id(self):
        return 5

    def download_data(self):
        url = 'http://napostu.ceskaposta.cz/vystupy/balikovny.xml'
        r = requests.get(url).content
        root = ET.fromstring(r)
        return root

    def load_data(self):
        root = self.download_data()
        for row in root.findall('.//ns:row', self.ns):
            id = row.find('ns:PSC', self.ns).text
            name = row.find('ns:NAZEV', self.ns).text
            address = row.find('ns:ADRESA', self.ns).text
            city = row.find('ns:OBEC', self.ns).text
            zip = row.find('ns:PSC', self.ns).text
            country = 'cz'
            latitude = row.find('ns:SOUR_Y_WGS84', self.ns).text
            longitude = row.find('ns:SOUR_X_WGS84', self.ns).text
            box = row.find('ns:TYP', self.ns).text == 'balíkovna-BOX'
            opening_hours = self.parse_opening_hours(row)
            card = True

            self.save_or_update_branch(id, name, address, city, country, zip, latitude, longitude, opening_hours, box, True)

    def parse_opening_hours(self, row):
        opening_hours = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [], "saturday": [],
                         "sunday": []}
        for day in row.find('ns:OTEV_DOBY', self.ns):
            current_day = self.day_map[day.attrib['name']]
            for op in day.findall('ns:od_do', self.ns):
                opening_hours[current_day].append(
                    {'open': op.find('ns:od', self.ns).text, 'close': op.find('ns:do', self.ns).text})
        return opening_hours
