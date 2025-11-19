def perform_operation(num1:float, num2:float, operation:str):
    match operation:
        case 'add':
            return num1+num2 
        case 'subtract': 
            return num1-num2 
        case 'multiply': 
            return num1*num2 
        case 'divide':
            if num2== 0 : 
                return 'cannot divide by 0 ' 
            else: 
                return num1/num2
        case _:
            return 'Not recognized as operation'