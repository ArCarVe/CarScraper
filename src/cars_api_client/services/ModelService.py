import requests
from cars_api_client.services.Service import Service


class ModelService(Service):

    def post(self, id, model, uri="/brand/id/models"):
        uri = uri.replace('id', str(id))
        response = requests.post(
            url=f"{self.url}{uri}",
            json=model
        )

        return response.json()