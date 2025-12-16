#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """
    Check the health of a plant based on its name, water level,
    and sunlight hours.

    Raises ValueError with a helpful message if any parameter is invalid.

    Args:
        plant_name (str): Name of the plant. Must not be empty.
        water_level (int): Water level (1-10).
        sunlight_hours (int): Hours of sunlight (2-12).
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")

    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is "
                         f"too high (max 12)")
    print("Plant 'tomato' is healthy!")


def test_plant_checks() -> None:
    """
    Test the check_plant_health function with valid and invalid data.

    Demonstrates raising and catching ValueError with informative messages.
    """
    # Test with valid values
    print("\nTesting good values...")
    try:
        check_plant_health("Tomato", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")

    # Test with empty plant name
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")

    # Test with invalid water level
    print("\nTesting bad water level...")
    try:
        check_plant_health("Rose", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")

    # Test with invalid sunlight hours
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Rose", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    # Program header
    print("=== Garden Plant Health Checker ===")
    # Run the test suite
    test_plant_checks()
