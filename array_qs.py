"""Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list."""
def sum_even(l):
    return sum([i for i in l if i%2 == 0])

#print(sum_even([1, 2, 3, 4, 5, 6]))



"""Write a Python function to reverse a given list without using the built-in reverse() method."""

def reverse_list(lst):

    reversed_list = []

    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

    
#print(reverse_list([1, 2, 3, 4, 5, 6]))


""" Given two lists, write a Python function that merges them and removes duplicates from the merged list."""

def merge_remove_duplicates(lst1, lst2):

    #return list(set(lst1+lst2))

    #return lst1 + [i for i in lst2 if i not in lst1]

    for item in lst2:
        if item not in lst1:
            lst1.append(item)

    return lst1

#print(merge_remove_duplicates([1, 2, 3], [3, 4, 5]))


"""Write a Python function that rotates a list to the right by n positions."""

def rotate_right(lst, n):
    n = n % len(lst)  
    print(lst[n:])
    return lst[-n:] + lst[:-n]

#print(rotate_right([1,2,3,4,5],2))

"""create a function that takes a 1D array and returns a new array where each element is multiplied by its index"""

def multiply_by_index(lst):
    result = [i * lst[i] for i in range(len(lst))]

    return result

#print(multiply_by_index([10, 20, 30, 40]))

"""Write a Python function that returns the sum of the diagonal elements of a 2D array."""
def diag_sum(lst):
    n = len(lst)
    sum = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                sum += lst[i][j]
    return sum

#print(diag_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

"""write a function that returns a new 2D array where all elements are replaced by their squared values."""


def sqr_items(lst):
    n = len(lst) 
    for i in range(n):
        for j in range(n):
            lst[i][j] = lst[i][j]*lst[i][j]
    
    return lst

#print(sqr_items([[1, 2], [3, 4]]))

"""Create a NumPy function that checks if a given 2D array is symmetric"""

def array_symmetric(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n):
            if lst[i][j] != lst[j][i]:
                return False 
    return True
            
# print(array_symmetric([[1, 2, 3], 
#           [2, 5, 6], 
#           [3, 6, 9]]))

"""Write a Python function that flattens a 3D array into a 1D array.""" 

def flatten_array(lst):
    return [element for row in lst for element in row]

# print(flatten_array([[1, 2, 3], 
#           [2, 5, 6], 
#           [3, 6, 9]]))

"""write a function that normalizes a 1D array"""

def norm_array(lst):
    min_val = min(lst)
    max_val = max(lst)
    
    return [round((x - min_val) / (max_val - min_val), 2) for x in lst]

#print(norm_array([2, 4, 6, 8]))


### Print only columns ### 

def print_columns(lst):
    
    n = len(lst)
    
    columns_only = []
    for r in range(n):
        column = []
        for c in range(n):
            column.append(lst[r][c])
        columns_only.append(column)
    return columns_only


# print(print_columns([[1, 2, 3], 
#           [2, 5, 6], 
#           [3, 6, 9]]))

# import random 

# rand_num = random.randint(1, 100)
# user_guess = 0

# while user_guess != rand_num:
#     user_guess = int(input("guess a num "))
#     if user_guess > rand_num:
#         print("Guess too high")
#     elif user_guess < rand_num:
#         print("Guess too Low")
#     else:
#         print(f"Congratulations {user_guess} is the correct guess")

"""Write a Python program that asks the user for a positive integer n and prints the first n numbers of the Fibonacci sequence using a while loop."""

def fibonacci(n):
    n1, n2 = 0, 1

    count = 0
    
    result = []
    while count < n:
        result.append(n1)
        n1, n2 = n2, n1 + n2 
        count += 1

    return result
        
print(fibonacci(7))
