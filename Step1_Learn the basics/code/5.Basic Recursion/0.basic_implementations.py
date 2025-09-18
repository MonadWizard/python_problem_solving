# Print Name N times using Recursion

def print_name(name, n):
    if n == 0:
        return
    print(name)
    print_name(name, n - 1)
    
print_name("Alice", 5)

print('\n---\n')


# Print 1 to N using Recursion
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)
    
print_1_to_n(5)

print('\n---\n')

# Print N to 1 using Recursion
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)

print_n_to_1(5)

print('\n---\n')


# print sum of first N natural numbers using Recursion
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))

print('\n---\n')



# reverse an array using Recursion 
# questing is not clear, assuming we need to create an array from 1 to N in reverse order, where N is given as input
def reverse_array(n, arr=[]):
    if n == 0:
        return arr
    arr.append(n)
    arr = reverse_array(n - 1, arr)
    return arr


print(reverse_array(5))

print('\n---\n')


# reverse a passing array using Recursion
# question is not clear, a function take only array and need to return the reversed array 
#  without taking data on global variable or take extra parameter

def reverse_passing_array(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + reverse_passing_array(arr[:-1])

print(reverse_passing_array([1, 2, 3, 4, 5]))





