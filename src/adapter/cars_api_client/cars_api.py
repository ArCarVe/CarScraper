from adapter.cars_api_client.services.GenerationService import GenerationService
from adapter.cars_api_client.services.BrandService import BrandService
from adapter.cars_api_client.services.ModelService import ModelService
from adapter.cars_api_client.services.CarService import CarService

class CarsApiClient:

    def __init__(self):
        self.generation_service = GenerationService()
        self.brand_service = BrandService()
        self.model_service = ModelService()
        self.car_service = CarService()

    def post_brand(self, brand):
        return self.brand_service.post(brand)
    
    def post_model(self, brand_id, model):
        return self.model_service.post(brand_id, model)
    
    def post_generation(self, model_id, generation):
        return self.generation_service.post(model_id, generation)

    def post_car(self, generation_id, car):
        return self.generation_service.post(generation_id, car)
