from bs4 import BeautifulSoup
import requests
from re import sub


class BaseScrapper:

    def __init__(self, base_url="https://www.auto-data.net"):
        self.base_url = base_url


    def get_soup_html_from(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.content, 'html.parser')

    def clear_string(self, input_string):
        return sub('[\n\r]', '', input_string)

    def extract_value_from_table(self, field_name, car_table):
        result = None
        try:
            table_head = car_table.find('th', text=field_name)
            table_data = table_head.parent.find("td")
            if field_name in table_head.text:
                result = self.clear_string(table_data.text)
        except Exception:
            print(f'The field: {field_name} is missing')
        
        return result