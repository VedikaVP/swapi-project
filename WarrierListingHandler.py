
from abc import ABC, abstractmethod
from ServicePackage.randgen import generate_number
from swapi01 import WarrierListingService


class WarrierListing(ABC):
    @abstractmethod
    def get_warrier_listing(self):
        pass

class WarrierListingHandeler(WarrierListing):
    response_dict = dict()

    def get_warrier_listing(self):
        # constant api
        host_url = "https://swapi.dev/api/"
        post_url = "people/{0}"
        # service api
        callapi = WarrierListingService()
        # random number generator
        random_id_list = generate_number().random_list(15, 1, 82)
        print(random_id_list)
        for num in random_id_list:
            complete_url = host_url + post_url.format(num)
            req = callapi.fetch(complete_url)
            self.response_dict[num] = req
            print(complete_url)
        print(self.response_dict)
        print(self.response_dict.keys())
        print(self.response_dict.values())


#--------------------------------------
objWarrier =  WarrierListingHandeler()
objWarrier.get_warrier_listing()


