def function_with_improved_error_handling(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
        raise TypeError("Invalid input types. Both inputs must be numbers.")
    if b == 0:
        raise ZeroDivisionError("Division by zero!")
    return a / b

# Demonstrating improved error handling

print(function_with_improved_error_handling(10,2))

try:
    print(function_with_improved_error_handling(10,0))
except ZeroDivisionError as e:
    print("Error:", e)

try:
    print(function_with_improved_error_handling(10,"hello"))
except TypeError as e:
    print("Error:", e)