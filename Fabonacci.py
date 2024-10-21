def fibonacci(n):
    fib_series = []
    a, b = 0, 1  # Starting values

    for _ in range(n):
        fib_series.append(a)  # Append current number to the series
        a, b = b, a + b  # Update a and b to the next two numbers

   
