# ERFAN MIRZAEE HW1 SUBMISION
  
# Question 1. 
# A program called calculator which has 4 function to add,subtract, # divide, multiply x, y ,z


from typing import Union

Number = Union[int, float]

def add(x: Number, y: Number, z: Number) -> Number:
    #this return x + y + z.
    return x + y + z

def subtract(x: Number, y: Number, z: Number) -> Number:
    #returns z - y - x
    return z - y - x

def divide(x: Number, y: Number) -> float:
    #returns x / y as a float.
    return x / y

def multiply(x: Number, y: Number) -> Number:
    #returns x * y.
    return x * y

def compute_expression(x: Number, y: Number, z: Number) -> float:

#This function will compute ((x+y+z)*x) / ((z-y-x)*y) using the #arithmetic helpers. Also denominator cant be zero so a if #statement in function helps
 
    numerator = multiply(add(x, y, z), x)
    denominator = multiply(subtract(x, y, z), y)

    if denominator == 0:
        raise ZeroDivisionError("Denominator is 0; cannot divide.")

    return divide(numerator, denominator)

if __name__ == "__main__":
    # Example usage
    x, y, z = 2, 3, 10
    try:
        result = compute_expression(x, y, z)
        print(f"For x={x}, y={y}, z={z}, result of ((x+y+z)*x)/(z-y-x)*y  = {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
