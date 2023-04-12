def fibonacci (n):
    
    # Check if input is less than 0 then it will print incorrect input
    if n < 0:
        print("Incorrect input")
    # Check if n is 0 then it will return 0
    elif n == 0:
        return 0
    # Check if n is 1 it will return 1
    elif n == 1 :
        return 1
    # the rest of the numbers goes under this case
    else:
        return fibonacci(n-1) + fibonacci(n-2)
