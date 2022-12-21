import requests
from cars_api_client.services.Service import Service


class GenerationService(Service):

    def post(self, id, generation, uri="/model/id/generations"):
        uri = uri.replace('id', str(id))
        response = requests.post(
            url=f"{self.url}{uri}",
            json=generation
        )

        return response.json()