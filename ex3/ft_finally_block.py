#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    """Open the watering system and water each plant in the list.

    Raises WaterError when a plant name is invalid (None in this
    exercise). The function prints actions (opening + watering) but
    does not handle errors itself: it raises them so the caller can
    decide how to handle cleanup and recovery.

    Args:
        plant_list (list): A list of plant names (strings) to water.
    """

    # Simulate opening the watering hardware or connection
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print(f"Error: cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Run two watering scenarios to demonstrate cleanup.

    - First scenario: a valid list where all plants are watered.
    - Second scenario: an invalid list containing None which causes
      WaterError to be raised. We use try/except/finally in both
      cases to show that cleanup (finally) always runs.
    """

    valid_list = ["tomato", "lettuce", "carrots"]
    invalid_list = ["tomato", None, "carrots"]

    # Normal case: expect no exceptions
    print("Testing normal watering...")
    water_plants(valid_list)
    print("\nTesting with error...")

    # Error case: water_plants will raise WaterError when it finds None
    water_plants(invalid_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    # Program entry point — print header and run the tests
    print("=== Garden Watering System ===\n")
    test_watering_system()
