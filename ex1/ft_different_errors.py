#!/bin/usr/env python

def garden_operations(error_type: str) -> None:
    """Trigger specific errors based on the provided type.

    Args:
        error_type (str): Type of error to raise. Options:
            "value", "division", "file", "key", "all".
    """
    if error_type == "value":
        int("abc")
    if error_type == "division":
        1 / 0
    if error_type == "file":
        open("missing.txt")
    if error_type == "key":
        var = {"rose": 1}
        var["missing_plant"]
    if error_type == "all":
        int("abc")
        1 / 0
        open("missing.txt")
        var = {"rose": 1}
        var["missing_plant"]


def test_error_types() -> None:
    """Test different error types and show how they are caught.

    This function demonstrates individual error handling, shows that
    execution continues after errors, and displays how to catch several
    error types with a single except block.
    """
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("division")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: "
              "No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("all")
    except (ValueError, ZeroDivisionError,
            FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")
