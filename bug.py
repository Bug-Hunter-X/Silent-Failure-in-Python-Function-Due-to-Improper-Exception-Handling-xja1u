def function_with_uncommon_bug(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
        return None  # Or raise a custom exception
    except TypeError:
        print("Invalid input types!")
        return None
    return result

# Demonstrating the bug:
print(function_with_uncommon_bug(10, 2))  # Output: 5.0
print(function_with_uncommon_bug(10, 0))  # Output: Division by zero! None
print(function_with_uncommon_bug(10, "hello")) # Output: Invalid input types! None

#Demonstrating the silent failure bug:
print(function_with_uncommon_bug(10, 0) * 2) #Output: None