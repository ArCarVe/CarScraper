from abc import abstractmethod
import requests


class Service():

    def __init__(self, url="http://localhost:8080"):
        self.url = url

    def post_request(self, uri, entity, **kwargs):
        uri = uri.replace('id', str(kwargs.get('id'))) if 'id' in kwargs.keys() else uri

        response = requests.post(url=f"{self.url}{uri}", json=entity)

        return response.json()

    @abstractmethod
    def post(self):
        pass


    # @abstractmethod
    # def get(self):
    #     pass

    # @abstractmethod
    # def put(self):
    #     pass

    # @abstractmethod
    # def delete(self):
    #     pass