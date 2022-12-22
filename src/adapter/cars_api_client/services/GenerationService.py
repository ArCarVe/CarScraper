from adapter.cars_api_client.services.Service import Service


class GenerationService(Service):

    def post(self, id, generation, uri="/model/id/generations"):
        return self.post_request(uri, generation, id=id)
