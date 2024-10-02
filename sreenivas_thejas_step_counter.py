class NegativeValueError(ValueError):
    pass

def steps_to_miles(steps):
    try:
        steps = int(steps)
        if steps < 0:
            raise NegativeValueError("Exception: Negative Step Count Entered.")
        miles = steps / 2000
        return miles
    except ValueError:
        raise ValueError("Exception: Non-Numeric Value Entered.")

try:
    user_input = input("Enter the number of steps: ")
    result = steps_to_miles(user_input)
    print(f'Miles walked: {result:.2f}')
except (ValueError, NegativeValueError) as x:
    print(x)
