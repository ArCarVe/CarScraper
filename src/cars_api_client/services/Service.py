from abc import abstractmethod


class Service():

    def __init__(self, url="http://localhost:8080"):
        self.url = url

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