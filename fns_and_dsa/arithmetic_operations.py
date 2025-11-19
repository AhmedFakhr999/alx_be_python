def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations using structural pattern matching.
    """
    match operation:
        case 'add':
            return num1 + num2 
        case 'subtract': 
            return num1 - num2 
        case 'multiply': 
            return num1 * num2 
            
        # Handles 'divide' with a Guard Clause for zero
        case 'divide' if num2 == 0:
            return 'cannot divide by 0'
            
        # Handles 'divide' for all other cases (num2 != 0)
        case 'divide':
            return num1 / num2
            
        case _:
            return 'Not recognized as operation'