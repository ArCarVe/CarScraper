import requests
from cars_api_client.services.Service import Service
from json import loads


class BrandService(Service):

    def post(self, brand, uri="/brands"):
        response = requests.post(
            url=f"{self.url}{uri}",
            json=brand
        )

        return response.json()