# Basic example of syntax, indentation, variables, and datatypes
def basic_example():
    """Demonstrates basic Python syntax, variables, and datatypes."""
    # Variable declarations
    name = "Alice"  # String
    age = 25        # Integer
    height = 5.6    # Float
    is_student = True  # Boolean

    # Printing variables
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}")
    print(f"Is Student: {is_student}")

# Call the basic example function
result = basic_example()

def explain_datatypes():
    """Explains all the major datatypes in Python with examples."""
    # Numeric types
    integer_example = 10  # Integer
    float_example = 10.5  # Float
    complex_example = 3 + 4j  # Complex number

    # Sequence types
    string_example = "Hello, World!"  # String
    list_example = [1, 2, 3, 4, 5]  # List
    tuple_example = (1, 2, 3, 4, 5)  # Tuple
    range_example = range(5)  # Range

    # Set types
    set_example = {1, 2, 3, 4, 5}  # Set
    frozenset_example = frozenset([1, 2, 3, 4, 5])  # Frozenset

    # Mapping type
    dict_example = {"key1": "value1", "key2": "value2"}  # Dictionary

    # Boolean type
    bool_example = True  # Boolean

    # None type
    none_example = None  # NoneType

    # Printing examples
    print("Numeric Types:")
    print(f"Integer: {integer_example}, Float: {float_example}, Complex: {complex_example}")
    print("\nSequence Types:")
    print(f"String: {string_example}, List: {list_example}, Tuple: {tuple_example}, Range: {list(range_example)}")
    print("\nSet Types:")
    print(f"Set: {set_example}, Frozenset: {frozenset_example}")
    print("\nMapping Type:")
    print(f"Dictionary: {dict_example}")
    print("\nBoolean Type:")
    print(f"Boolean: {bool_example}")
    print("\nNone Type:")
    print(f"None: {none_example}")

# Call the function to explain datatypes
explain_datatypes()