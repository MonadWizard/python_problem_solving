# 1) Sum of an Array
# Problem: Return the sum of all numbers in a list.

def sum_array(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])


print(f"Sum of array: {sum_array([1, 2, 3, 4, 5])}")  # Output: 15




# 2) Factorial of a Number
# Problem: Return the factorial of a given number.

def factorial(n):
    if n < 0:
        return "Invalid input, input must be a non-negative integer."
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(f"Factorial: {factorial(-5)}")  # Output: 120
print(f"Factorial: {factorial(5)}")  # Output: 120



# fibonacci sequence
# Problem: Return the nth Fibonacci number.

def fibonacci(n):
    if n < 0:
        return "Invalid input, input must be a non-negative integer."
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci: {fibonacci(-5)}")  # Output: 0
print(f"Fibonacci: {fibonacci(5)}")  # Output: 5



# Binary Search
# Problem: Given a sorted array and a target value, return the index of the target value in the array. If the target value is not found, return -1.










# DFS on a Tree
# Problem: Given a binary tree, return the inorder traversal of its nodes' values.



