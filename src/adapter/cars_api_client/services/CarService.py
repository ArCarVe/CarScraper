from adapter.cars_api_client.services.Service import Service


class CarService(Service):

    def post(self, id, car, uri="/generation/id/cars"):
        return self.post_request(uri, car, id=id)
