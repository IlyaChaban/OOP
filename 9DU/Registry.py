from typing import List
"""
    vvvv      YOUR SOLUTION      vvvv
"""


class Person:

    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name 
        self.surname = surname
        self.age = age
        self._vehicle_count = 0
    def __eq__(self, other: 'Person') -> bool:
        return True if self.name == other.name and self.surname == other.surname and self.age == self.age else False
        
    def get_vehicle_count(self) -> int:
        return self._vehicle_count

class Vehicle:

    def __init__(self, registration_plate: str, creation_date: str, owner: Person) -> None:
        self.registration_plate = registration_plate
        self.creation_date = creation_date
        self.owner = owner
        
    def __eq__(self, other: 'Vehicle') -> bool:
        return True if self.registration_plate == other.registration_plate else False

class Register:

    def __init__(self) -> None:
        self.registered_vehicles = []
        self.registered_owners = []
        
    def insert_vehicle(self, vehicle: Vehicle) -> int:
        
        for registered_vehicle in self.registered_vehicles:
            if registered_vehicle == vehicle:
                return 0
        
        self.registered_vehicles.append(vehicle)
        
        self.insert_owner(vehicle.owner)
        return 1
    
    def insert_owner(self, owner: Person):
        
        for registered_owner in self.registered_owners:
            if registered_owner == owner:
                owner._vehicle_count = owner.get_vehicle_count() + 1
                return 0
                
        self.registered_owners.append(owner)
        owner._vehicle_count = owner.get_vehicle_count() + 1
        return 1
    
    def update_vehicle_owner(self, registration_plate: str, new_owner: Person) -> int:
        old_owner = None
        for registered_vehicle in self.registered_vehicles:
            if registered_vehicle.registration_plate == registration_plate:
                if registered_vehicle.owner != new_owner:
                    
                    registered_vehicle.owner._vehicle_count = registered_vehicle.owner.get_vehicle_count() - 1
                    old_owner = registered_vehicle.owner
                    registered_vehicle.owner = new_owner
                    registered_vehicle.owner._vehicle_count = registered_vehicle.owner.get_vehicle_count()+1
                    
                    if old_owner.get_vehicle_count() == 0:
                        self.registered_owners.pop(self.registered_owners.index(old_owner))
                    
                    
                    return 1
        return 0

    def delete_vehicle(self, registration_plate: str) -> int:
        for registered_vehicle in self.registered_vehicles:
            if registered_vehicle.registration_plate == registration_plate:
                self.registered_vehicles.pop(self.registered_vehicles.index(registered_vehicle))
                registered_vehicle.owner._vehicle_count = registered_vehicle.owner.get_vehicle_count()-1
                if registered_vehicle.owner.get_vehicle_count() == 0:
                    self.registered_owners.pop(self.registered_owners.index(registered_vehicle.owner))
                return 1
        return 0
                
                
    def list_vehicles(self) -> List[Vehicle]:
        return self.registered_vehicles

    def list_owners(self) -> List[Person]:
        return self.registered_owners

    def list_vehicle_by_owner(self, owner: Person) -> List[Vehicle]:
        result = []
        for registered_vehicle in self.registered_vehicles:
            if registered_vehicle.owner == owner:
                result.append(registered_vehicle)
        return result


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


register = Register()

person1 = Person("John", "Doe", 20)
person2 = Person("Alice", "Doe", 22)

car1 = Vehicle("abc0", "20221122", person1)
car2 = Vehicle("abc1", "20221123", person1)
car3 = Vehicle("abc0", "20221122", person1)
car4 = Vehicle("xyz", "20221124", person2)

# car1 = Vehicle("abc", "20221122", person1)

# test insertion
assert register.insert_vehicle(car1) == 1
assert register.insert_vehicle(car2) == 1
assert register.insert_vehicle(car3) == 0
assert register.insert_vehicle(car4) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 2 and register.list_owners()[1].get_vehicle_count() == 1

# test update
assert register.update_vehicle_owner("abc1", person1) == 0
assert register.update_vehicle_owner("not in register", person1) == 0
assert register.update_vehicle_owner("abc1", person2) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person2), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 1 and register.list_owners()[1].get_vehicle_count() == 2
assert register.update_vehicle_owner("abc0", person2) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person2), Vehicle("abc1", "20221123", person2), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 3

# test delete
assert register.delete_vehicle("not in register") == 0
assert register.delete_vehicle("abc0") == 1
assert register.delete_vehicle("abc1") == 1
assert register.delete_vehicle("xyz") == 1
assert register.list_vehicles() == []
assert register.list_owners() == []

# test lists
car1 = Vehicle("abc0", "20221122", person1)
car2 = Vehicle("abc1", "20221123", person1)
car3 = Vehicle("abc0", "20221122", person1)
car4 = Vehicle("xyz", "20221124", person2)

register.insert_vehicle(car1)
register.insert_vehicle(car2)
register.insert_vehicle(car3)
register.insert_vehicle(car4)

assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)]
assert register.list_vehicle_by_owner(person1) == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1)]