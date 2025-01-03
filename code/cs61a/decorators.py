def trace1(fn):
    def traced(x):
        print("Before the function call")
        result = print(fn(x))
        print("After the function call")
        return result

    return traced  # Ensure the wrapper function is returned


# Original function
def square(x):
    return x * x


# Manually applying the decorator
decorated_square = trace1(square)
decorated_square(5)  # Output: Decorator applied manually


# Using the decorator with @ syntax
@trace1
def square_with_decorator(x):
    return x * x


square_with_decorator(6)  # Output: Decorator applied via @trace1
