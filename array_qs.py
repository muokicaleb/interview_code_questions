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

