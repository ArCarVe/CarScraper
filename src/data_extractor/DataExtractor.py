from scraper.AutoDataScraper import AutoDataScraper
from cars_api_client.cars_api import CarsApiClient


class DataExtractor:

    def __init__(self):
        self.scraper = AutoDataScraper()
        self.api = CarsApiClient()

    def extract(self):
        for brand, brand_href in self.scraper.brands_extractor():
            print(brand)
            brand_db = self.api.post_brand(brand)

            print('brandDB', brand_db)

            for model, model_href in self.scraper.brand_models_extractor(brand_href):
                print(model)
                model_db = self.api.post_model(brand_db['brandId'], model)

                print('modelDB', model_db)

                for generation, generation_href in self.scraper.models_generations_extractor(model_href):
                    
                    print(generation)
                    generation_db = self.api.generation_service.post(model_db['modelId'], generation)

                    print('generationDB', generation_db)

                    for modification_href in self.scraper.generation_modifications_extractor(generation_href):

                        car = self.scraper.car_data_extractor(modification_href)
                        print(car)
                    break
                

