#!/usr/bin/env python3

"""Garden watering system demo with finally cleanup.

This file keeps your original logic exactly as you wrote it but adds
educational comments, docstrings and type hints. Lines are wrapped to
stay within 79 columns where possible.
"""


class WaterError(Exception):
    """Custom exception raised for watering-related problems."""
    pass


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
    for plant in plant_list:
        # Validate the plant entry; here None means invalid
        if plant is None:
            # Raise a descriptive error; message intentionally left
            # identical to your original string so output doesn't change
            raise WaterError(
                f"Cannot watter {plant} - invalid plant!"
            )
        # Normal action: watering this plant
        print(f"Watering {plant}")


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
    try:
        water_plants(valid_list)
    except WaterError as e:
        # If something unexpected happens, show the error message
        print(e)
    finally:
        # Cleanup logic that must always run (close system, free
        # resources, etc.)
        print("Closing watering system (cleanup)")

    print("\nTesting with error...")

    # Error case: water_plants will raise WaterError when it finds None
    try:
        water_plants(invalid_list)
    except WaterError as e:
        # Print the error message produced by the raise in
        # water_plants(). The caller chooses how to handle it.
        print(e)
    finally:
        # This finally always executes, demonstrating guaranteed cleanup
        print("Closing watering system (cleanup)")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    # Program entry point — print header and run the tests
    print("=== Garden Watering System ===\n")
    test_watering_system()
