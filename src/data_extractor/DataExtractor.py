from scraper.AutoDataScraper import AutoDataScraper
from cars_api_client.cars_api import CarsApiClient


class DataExtractor:

    def __init__(self):
        self.scraper = AutoDataScraper()
        self.api = CarsApiClient()


    def _extract_data(self):
        for brand, brand_href in self.scraper.brands_extractor():
            brand_db = self.api.post_brand(brand)

            self._extract_models(brand_db.get('brandId'), brand_href)

    def _extract_models(self, brand_id, brand_href):
        for model, model_href in self.scraper.brand_models_extractor(brand_href):
            model_db = self.api.post_model(brand_id, model)

            self._extract_generations(model_db.get('modelId'), model_href)

    def _extract_generations(self, model_id, model_href):
        for generation, generation_href in self.scraper.models_generations_extractor(model_href):
            generation_db = self.api.generation_service.post(model_id, generation)

            self._extract_modifications(generation_db.get('generationId'), generation_href)   

    def _extract_modifications(self, generation_id, generation_href):
        modifications = self.scraper.generation_modifications_extractor(generation_href) 
        if modifications:
            for modification_href in modifications:
        
                car = self.scraper.car_data_extractor(modification_href)
                self.api.car_service.post(generation_id, car)
    
    def extract(self):
        self._extract_data()
