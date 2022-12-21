from scraper.AutoDataScraper import AutoDataScraper
from cars_api_client.cars_api import CarsApiClient


class DataExtractor:

    def __init__(self):
        self.scraper = AutoDataScraper()
        self.api = CarsApiClient()

    def extract(self):
        for brand, brand_href in self.scraper.brands_extractor():
            brand_db = self.api.post_brand(brand)

            for model, model_href in self.scraper.brand_models_extractor(brand_href):
                model_db = self.api.post_model(brand_db['brandId'], model)

                for generation, generation_href in self.scraper.models_generations_extractor(model_href):
                    generation_db = self.api.generation_service.post(model_db['modelId'], generation)

                    for modification_href in self.scraper.generation_modifications_extractor(generation_href):

                        car = self.scraper.car_data_extractor(modification_href)
                        car_db = self.api.car_service.post(generation_db['generationId'], car)
                

