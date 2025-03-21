def examples_collections():
    """Demonstrates examples using lists, tuples, sets, and dictionaries."""

    # List example
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")  # Adding an element
    print("List Example:")
    print(f"Fruits: {fruits}")

    # Tuple example
    coordinates = (10, 20, 30)
    print("\nTuple Example:")
    print(f"Coordinates: {coordinates}")

    # Set example
    unique_numbers = {1, 2, 3, 4, 5}
    unique_numbers.add(6)  # Adding an element
    print("\nSet Example:")
    print(f"Unique Numbers: {unique_numbers}")

    # Dictionary example
    student = {"name": "Alice", "age": 25, "grade": "A"}
    student["age"] = 26  # Updating a value
    print("\nDictionary Example:")
    print(f"Student: {student}")

# Call the function to demonstrate examples
examples_collections()

def documentation_collections():
    """Provides guidance on when to use lists, tuples, sets, and dictionaries."""
    print("When to use:")
    print("\nList:")
    print("- Use when you need an ordered collection of items that can be modified (mutable).")
    print("- Suitable for storing items where duplicates are allowed.")
    print("- Example: A list of fruits or tasks.")

    print("\nTuple:")
    print("- Use when you need an ordered collection of items that cannot be modified (immutable).")
    print("- Suitable for fixed data like coordinates or configuration values.")
    print("- Example: A tuple representing a point in 3D space.")

    print("\nSet:")
    print("- Use when you need an unordered collection of unique items.")
    print("- Suitable for operations like union, intersection, and difference.")
    print("- Example: A set of unique numbers or tags.")

    print("\nDictionary:")
    print("- Use when you need to store key-value pairs for fast lookups.")
    print("- Suitable for mapping relationships like a student's name to their grade.")
    print("- Example: A dictionary storing user details or configuration settings.")

# Call the function to display documentation
documentation_collections()
