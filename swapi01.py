import requests
from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def fetch(self, url):
        pass

class WarrierListingService(Service):
    def fetch(self, url):
        req = requests.get(url)
        return req.json()

