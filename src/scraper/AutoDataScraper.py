from scraper.BaseScraper import BaseScrapper
from cars_api_client.cars_api import CarsApiClient
from models.Generation import Generation
from models.Brand import Brand
from models.Model import Model
from models.Car import Car
from utils.Utils import Utils


class AutoDataScraper(BaseScrapper):

    def __init__(self, base_url="https://www.auto-data.net"):
        super().__init__(base_url)
        self.api = CarsApiClient()

    def brands_extractor(self):
        html = self.get_soup_html_from(f"{self.base_url}/en/allbrands")
        brands_divs = html.find_all('div', class_="brands")
        for brand in brands_divs:
            for brand_tag in brand.find_all('a', class_="marki_blok"):
                if brand_tag.text.startswith('A'):
                    yield Brand(self.clear_string(brand_tag.text)).to_json(), brand_tag['href']

    def brand_models_extractor(self, href):
        brand_models_html = self.get_soup_html_from(f"{self.base_url}{href}")
        for model_tag in brand_models_html.find_all('a', class_="modeli"):
            yield Model(self.clear_string(model_tag.text)).to_json(), model_tag['href']

    def get_generations_rows(self, html):
        if len(html.find_all('tr', class_="lgreen")) > 0:
            return html.find_all('tr', class_="lgreen")
        return html.find_all('tr', class_="lred")

    def get_generation_start_end(self, a_tag):
        if a_tag.find('strong', class_="end"):
            return a_tag.find('strong', class_="end").text.split(' - ')
        return a_tag.find('strong', class_="cur").text.split(' - ')

    def get_start_end_production_years(self, a_tag):
        generation_years = self.get_generation_start_end(a_tag)

        return Utils.get_int_value_from_string(generation_years[0]), \
            Utils.get_int_value_from_string(generation_years[1])

    def models_generations_extractor(self, href):
        model_generations_html = self.get_soup_html_from(f"{self.base_url}{href}")

        for generation in self.get_generations_rows(model_generations_html):
            start, end = self.get_start_end_production_years(generation.find('td').find('a'))
            gen = generation.find('th').find('a')
            yield Generation(self.clear_string(gen.text), start, end).to_json(), gen['href']
    
    def generation_modifications_extractor(self, href):
        modifications_html = self.get_soup_html_from(f"{self.base_url}{href}")
        modifications_table = modifications_html.find(id="outer").find('table')
        for modification in modifications_table.find_all('a'):
            if modification.find('span', class_="tit"):
                yield modification['href']
    
    def car_data_extractor(self, href):
        car_html = self.get_soup_html_from(f"{self.base_url}{href}")
        car_table = car_html.find(id="outer").find('table', class_="cardetailsout")

        modification = self.extract_value_from_table('Modification (Engine) ', car_table).split(' (')

        return Car(
            modification=modification[0],
            is_automatic='Automatic' in modification[1],
            seats=Utils.get_int_value_from_string(self.extract_value_from_table('Seats ', car_table)),
            doors=Utils.get_int_value_from_string(self.extract_value_from_table('Doors ', car_table)),
            hp=Utils.get_int_value_from_string(modification[1].split('Hp')[0])
        ).to_json()
