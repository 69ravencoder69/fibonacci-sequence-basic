# Fibonacci sequence using iterative approach

def fibonacci(n):
    # Initialize the first two terms
    a, b = 0, 1
    sequence = []
    
    # Generate the Fibonacci sequence up to n terms
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # Update a and b for the next iteration
    
    return sequence

# Input: Number of terms to generate in Fibonacci sequence
num_terms = int(input("Enter the number of terms in Fibonacci sequence: "))

# Output: Fibonacci sequence
fib_sequence = fibonacci(num_terms)
print("Fibonacci Sequence:", fib_sequence)
