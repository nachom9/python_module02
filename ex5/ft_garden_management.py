#!/usr/bin/env python3

class PlantError(Exception):
    """Base exception for plant-specific problems."""
    pass


class WaterError(PlantError):
    """Raised when a plant has an invalid water level."""
    pass


class SunlightError(PlantError):
    """Raised when a plant has an invalid sunlight amount."""
    pass


class GardenError(Exception):
    """Base exception for garden-level problems (tank, space, etc.)."""
    pass


class SpaceError(GardenError):
    """Raised when the garden exceeds a reasonable number of plants."""
    pass


class TankError(GardenError):
    """Raised when the garden water tank has insufficient water."""
    pass


class ErrorChecks:
    """Utility checks used before modifying garden state.

    These are simple helpers; they don't modify state — they only
    validate input and raise when something is wrong.
    """

    @staticmethod
    def plant_name_check(name: str) -> None:
        """Validate that a plant name is not empty.

        Raises:
            ValueError: If the provided name is empty.
        """
        if not name:
            raise ValueError("Plant name cannot be empty!")


class CheckPlant:
    """Validation helpers for individual plant attributes."""

    @staticmethod
    def water_level(water_level: int) -> None:
        """Validate a single plant's water level.

        Raises:
            WaterError: If water_level is out of the allowed range.
        """
        if water_level > 10:
            raise WaterError(
                f"Water level {water_level} is too high (max 10)"
            )
        elif water_level < 1:
            raise WaterError(
                f"Water level {water_level} is too low (min 1)"
            )

    @staticmethod
    def sunlight(sunlight: int) -> None:
        """Validate a single plant's sunlight hours.

        Raises:
            SunlightError: If sunlight is outside the allowed range.
        """
        if sunlight > 12:
            raise SunlightError(
                f"Sunlight level {sunlight} "
                f"is too high (max 12)"
            )
        elif sunlight < 2:
            raise SunlightError(
                f"Sunlight level {sunlight} "
                f"is too low (min 2)"
            )


class GardenManager:
    """A manager that holds plants and provides garden operations.

    Attributes:
        garden (list): Class-level list containing all plant instances.
        water_tank (int): Class-level water tank units available.
        plant_number (int): Class-level counter of plants added.
    """

    garden = []
    water_tank = 3
    plant_number = 0

    def __init__(self, name: str, water_level: int, sunlight: int) -> None:
        # Instance attributes describe each plant
        self.name = name
        self.water_level = water_level
        self.sunlight = sunlight

    def add_plant(self) -> None:
        """Validate and add this plant to the shared garden list.

        The name check raises ValueError on invalid input; the caller
        prints a helpful message and the function exits without adding
        the plant in that case.
        """
        try:
            ErrorChecks.plant_name_check(self.name)
            GardenManager.garden.append(self)
            GardenManager.plant_number += 1
            print(f"Added {self.name} successfully")
        except ValueError as e:
            # Keeps behavior identical to the version you wrote
            print("Error adding plant:", e)

    @classmethod
    def water_plants(cls) -> None:
        """Open watering system, attempt to water all plants, always
        close system at the end.

        Each plant is watered in-turn; if the shared tank runs out a
        TankError is raised for that plant and handled so the loop
        continues for subsequent plants.
        """
        print("Watering plants...\nOpening watering system")
        for plant in cls.garden:
            try:
                # Check shared tank before watering this plant
                if cls.water_tank < 1:
                    raise TankError("Not enough water in tank")
                print(f"Watering {plant.name} - success")
                cls.water_tank -= 1
            except TankError as e:
                # Handle the error for this plant and continue
                print(f"Error watering {plant.name}", e)
        # Always print the closing message (cleanup)
        print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Check this plant's health by validating water and sun.

        Prints a header for the check, then reports specific errors if
        either validation fails. If both validations pass, the plant is
        reported as healthy.
        """
        print("Checking plant health...")
        flag = True
        try:
            CheckPlant.water_level(self.water_level)
        except WaterError as e:
            print(f"Error checking {self.name}:", e)
            flag = False
        try:
            CheckPlant.sunlight(self.sunlight)
        except SunlightError as e:
            print(f"Error checking {self.name}:", e)
            flag = False
        finally:
            # If no errors were raised, flag remains True and we print
            if flag:
                print(
                    f"{self.name}: healthy (water: {self.water_level}, "
                    f"sun: {self.sunlight})"
                )

    @classmethod
    def check_garden(cls) -> None:
        """Perform garden-level checks and demonstrate recovery.

        Checks the shared water tank and total plant count. Any
        detected GardenError is reported and recovery is simulated in
        the final block.
        """
        print("Testing error recovery..")
        flag = True
        try:
            if cls.water_tank < 1:
                raise TankError("Not enough water in tank")
        except TankError as e:
            print("Caught GardenError:", e)
            flag = False
        try:
            if cls.plant_number > 5:
                raise SpaceError("Garden has too many plants")
        except SpaceError as e:
            print("Caught GardenError:", e)
            flag = False
        finally:
            if flag:
                print("No GardenError found. Everything is okay!")
            print("System recovered and continuing...")


if __name__ == "__main__":
    # Program header and demo run — your original flow preserved
    print("=== Garden Management System ===\n")
    tomato = GardenManager("Tomato", 5, 80)
    lettuce = GardenManager("Lettuce", 15, 8)
    nonvalid = GardenManager("", 5, 8)

    print("Adding plants to garden...")
    tomato.add_plant()
    lettuce.add_plant()
    nonvalid.add_plant()
    print("")
    GardenManager.water_plants()
    print("")
    tomato.check_plant_health()
    lettuce.check_plant_health()
    print("")
    GardenManager.check_garden()
    print("\nGarden management system test complete!")
