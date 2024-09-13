"""
You are given a list of integers as an input. Return a list with the same elements where all zeros are at the end of the array.


"""

def move_zeros(list_integers):

    non_zero = [i for i in list_integers if i != 0]
    
    zeros = [0]*(len(list_integers)-len(non_zero)) 

    return non_zero + zeros

input_list = [1, 0, 2, 0, 4, 3] 

print(move_zeros(input_list))  
