#!/usr/bin/env python

def check_temperature(temp_str: str) -> int | None:
    """
    Validate a temperature reading provided as a string.

    - Prints the temperature being tested
    - Converts the value to an integer
    - Prints error messages for invalid or extreme values
    - Prints a success message when temperature is acceptable
    - Returns the temperature if valid, otherwise None
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error, {temp_str} is not a number")
        return None
    else:
        if temp < 0:
            print(f"Error: {temp}ºC is too cold for plants (min 0ºC)")
            return None
        if temp > 40:
            print(f"Error: {temp}ºC is too hot for plants (max 40ºC)")
            return None
        else:
            print(f"Temperature {temp}ºC is perfect for plants!")
            return temp


def test_temperature_input() -> None:
    """
    Run sample tests to demonstrate temperature validation.
    """
    print("=== Garden Temperature Checker ===\n")
    check_temperature('25')
    print("")
    check_temperature('abc')
    print("")
    check_temperature('100')
    print("")
    check_temperature('-50')
    print("")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
