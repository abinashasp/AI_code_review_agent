def add(a, b):
    """
    TODO: Describe what add does.
    """

    return a + b

def subtract(a, b):
    """
    TODO: Describe what subtract does.
    """

    return a - b

def multiply(a, b):
    """
    TODO: Describe what multiply does.
    """

    return a * b

def divide(a, b):
    """
    TODO: Describe what divide does.
    """

    if b != 0:
        return a / b
    else:
        print("Division by zero not allowed")

def main():
    """
    TODO: Describe what main does.
    """

    x = 10
    y = 5
    print("Add:", add(x, y))
    print("Subtract:", subtract(x, y))
    print("Multiply:", multiply(x, y))
    print("Divide:", divide(x, y))

main()
