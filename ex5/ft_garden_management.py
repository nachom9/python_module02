#!/usr/bin/env python3

class GardenError(Exception):

    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):

    def __init__(self, message):
        super().__init__("Not enough water in the tank")


class GardenManager:

    def __init__(self, name, water_tank):

        self.name = name
        self.water_tank = water_tank
        self.plants = {}

    def add_plants(self, plants):

        for plant in plants:
            try:
                if not plants[plant].name:
                    raise ValueError("Plant name cannot be empty!")
                self.plants[plants[plant].name] = plants[plant]
                print(f"Added {plants[plant].name} successfully!")
            except ValueError as error:
                print(f"Error adding plant: {error}")

    def water_plants(self):

        try:
            for plant in self.plants:
                if self.water_tank < 1:
                    raise WaterError("")
                self.plants[plant].water_plant()
                self.water_tank -= 1
        except WaterError as error:
            print(f"Caught GardenError: {error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plants_health(self):

        for plant in self.plants:
            try:
                self.plants[plant].check_health()
            except ValueError as error:
                print(f"Error checking {plant}: {error}")

    def check_garden(self):

        try:
            if self.water_tank < 10:
                raise WaterError("")
        except WaterError as error:
            print(f"Caught GardenError: {error}")


class Plant:

    def __init__(self, name, water, sun):

        self.name = name
        self.water = water
        self.sun = sun

    def water_plant(self):

        self.water += 1
        print(f"Watering {self.name} - success")

    def check_health(self):

        if self.water < 1:
            raise ValueError(f"Water level {self.water} is too low (min 1)")
        if self.water > 10:
            raise ValueError(f"Water level {self.water} is too high (max 10)")
        if self.sun < 2:
            raise ValueError(f"Sunlight hours {self.sun} is too low (min 2)")
        if self.sun > 12:
            raise ValueError(f"Sunlight hours {self.sun} is too high (max 12)")
        print(f"{self.name}: healthy (water: {self.water}, sun: {self.sun})")


def main():

    print("=== Garden Management System ===\n")
    tomato = Plant("Tomato", 5, 8)
    lettuce = Plant("Lettuce", 15, 5)
    none_plant = Plant(None, 5, 5)
    plants = {'tomato': tomato,
              'lettuce': lettuce,
              'none_plant': none_plant
              }
    garden = GardenManager("My garden", 5)
    print("Adding plants to garden...")
    garden.add_plants(plants)
    print("\nWatering plants...")
    garden.water_plants()
    print("\nChecking plant health...")
    garden.check_plants_health()
    print("\nTesting error recovery...")
    garden.check_garden()
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
