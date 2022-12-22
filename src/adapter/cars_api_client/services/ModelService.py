from adapter.cars_api_client.services.Service import Service


class ModelService(Service):

    def post(self, id, model, uri="/brand/id/models"):
        return self.post_request(uri, model, id=id)
