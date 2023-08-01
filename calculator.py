def calculator():
    while True:
        try:
            user_input = input("Enter the expression (e.g. 2+2+4 or 3-4-2), or 'q' to quit: ")
            
            if user_input.lower() == 'q':
                break
            
            # Validate the input to contain only allowed characters and numbers
            allowed_chars = set('0123456789+-*/ ')
            if not set(user_input).issubset(allowed_chars):
                raise ValueError("Invalid characters in the input.")
            
            # Evaluate the expression using eval() function
            result = eval(user_input)
            print("Result:", result)
        
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()
