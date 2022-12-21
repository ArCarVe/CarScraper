from cars_api_client.services.GenerationService import GenerationService
from cars_api_client.services.BrandService import BrandService
from cars_api_client.services.ModelService import ModelService

class CarsApiClient:

    def __init__(self):
        self.generation_service = GenerationService()
        self.brand_service = BrandService()
        self.model_service = ModelService()

    def post_brand(self, brand_name):
        return self.brand_service.post(brand_name)
    
    def post_model(self, brand_id, model_name):
        return self.model_service.post(brand_id, model_name)
    
    def post_generation(self, model_id, generation_name):
        return self.generation_service.post(model_id, generation_name)
