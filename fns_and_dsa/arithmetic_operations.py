def perform_operation(num1, num2, operation):
   
  match operation:

    case 'add':
      return num1 + num2
      
    case 'subtract':
      return num1 - num2

    case 'multiply':
      return num1 * num2
    
    case 'divide':

      if num2 == 0:
        print("You cannot divide by zero.")
        return Null
      
      elif num2 != 0:
        return num1 / num2

    case _:
      print('Invalid operation')
      return Null