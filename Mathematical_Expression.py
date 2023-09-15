def evaluate(expression):
    chars = ["[", "]", "{", "}"]
    
    for char in chars:
        if char in expression:
            raise ValueError(f"{char} is not allowed in the expression.")
        
    try:
        result = eval(expression)
        return result

    except ZeroDivisionError:
        return "Division by zero is not allowed."

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    
try:
    user_input = input("Enter a mathematical expression: ")
    result = evaluate(user_input)
    print(f"Result of '{user_input}' is: {result}")

except ValueError as ve:
    print(f"Error: {ve}")