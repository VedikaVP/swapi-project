import requests

url = "https://swapi.dev/api/films/1/"
#" url for first film."
payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

film1_data = response.json()
print(film1_data)

print("*" * 15)

character_data = film1_data["characters"]
print(character_data)




class Film1character:
    names = []

    def get_name(self,list1):
        num = 0
        while num < len(list1):
            char_responce = requests.get(list1[num]).json()
            num = num+1
            name= char_responce.get("name")
            if name:
                self.names.append(name)
        print(self.names)


obj_characterfilm1 =   Film1character()
obj_characterfilm1.get_name(character_data)

planet_data = film1_data["planets"]
print(planet_data)
class planetslist:
    planets = []
    def get_planets(self, list2):
        num = 0
        while num < len(planet_data):
            planet_responce = requests.get(planet_data[0]).json()
            num = num+1
            planet = planet_responce.get("name")
            if planet:
                self.planets.append(planet)
        print(self.planets)

obj_planetfilm1 = planetslist()
obj_planetfilm1.get_planets(planet_data)

vehicles_data = film1_data["vehicles"]
print(vehicles_data)

class vehicle_list:
    vehicle = []
    def get_vehicle(self, list_):
        num = 0
        while num < len(list_):
            vehilce_responce = requests.get(list_[num]).json()
            num = num + 1
            vehicle_=  vehilce_responce.get("name")
        if vehicle_:
            self.vehicle.append(vehicle_)
        print(self.vehicle)



objvehicle = vehicle_list()
objvehicle.get_vehicle(vehicles_data)
