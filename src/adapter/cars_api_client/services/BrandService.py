from adapter.cars_api_client.services.Service import Service


class BrandService(Service):

    def post(self, brand, uri="/brands"):
        return self.post_request(uri, brand)
