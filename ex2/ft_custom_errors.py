#!/usr/bin/env python3

class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific problems."""
    pass


class WaterError(GardenError):
    """Exception raised when there is a watering problem."""
    pass


def water_check(water_level: int) -> None:
    """Check if water level is sufficient; raise WaterError if too low.

    Args:
        water_level (int): Current water level in the tank.

    Raises:
        WaterError: If water_level is below 5.
    """
    if water_level < 5:
        raise WaterError("Not enough water in the tank")


def plant_check(plant_name: str, health_status: str) -> None:
    """Check the health status of a plant; raise PlantError if wilting.

    Args:
        plant_name (str): Name of the plant.
        health_status (str): Current health status of the plant.

    Raises:
        PlantError: If health_status is 'wilting'.
    """
    if health_status == "wilting":
        raise PlantError(f"The {plant_name} plant is wilting!")


def garden_check(condition: str) -> None:
    """Raise a generic GardenError for general garden problems.

    Args:
        condition (str): Condition of the garden.

    Raises:
        GardenError: If the garden condition indicates a problem.
    """
    if condition == "damaged":
        raise GardenError("Your garden is damaged!")


def garden_errors_demo():
    print("=== Custom Garden Errors Demo ===\n")

    """ Demonstrate PlantError, WaterError and catching all garden errors
    """
    try:
        print("Testing PlantError...")
        plant_check("tomato", "wilting")
    except PlantError as e:
        print(f"Caught a garden error: {e}")
    print("")

    try:
        print("Testing WaterError...")
        water_check(3)
    except WaterError as e:
        print(f"Caught a garden error: {e}")
    print("")

    print("Testing catching all garden errors...")
    try:
        plant_check("tomato", "wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_check(3)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        garden_check("damaged")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    garden_errors_demo()
