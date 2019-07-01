# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Spyder Editor
# 
# This is a temporary script file.
# """
# import timeit 
#   
# # code snippet to be executed only once 
# mysetup = "from math import sqrt"
#   
# # code snippet whose execution time is to be measured 
# mycode = ''' 
# def example(): 
#     mylist = [] 
#     for x in range(100): 
#         mylist.append(sqrt(x)) 
# '''
#   
# # timeit statement 
# print ("execution time is", timeit.timeit(setup = mysetup, 
#                     stmt = mycode, 
#                     number = 10000))
# =============================================================================
# =============================================================================
# import timeit 
#   
# # binary search function 
# def binary_search(mylist, find): 
#     while len(mylist) > 0: 
#         mid = (len(mylist))//2
#         if mylist[mid] == find: 
#             return True
#         elif mylist[mid] < find: 
#             mylist = mylist[:mid] 
#         else: 
#             mylist = mylist[mid + 1:] 
#     return False
#   
#   
# # linear search function 
# def linear_search(mylist, find): 
#     for x in mylist: 
#         if x == find: 
#             return True
#     return False
#   
#   
# # compute binary search time 
# def binary_time(): 
#     SETUP_CODE = ''' 
# from __main__ import binary_search 
# from random import randint'''
#   
#     TEST_CODE = ''' 
# mylist = [x for x in range(10000)] 
# find = randint(0, len(mylist)) 
# binary_search(mylist, find)'''
#       
#     # timeit.repeat statement 
#     times = timeit.repeat(setup = SETUP_CODE, 
#                           stmt = TEST_CODE, 
#                           repeat = 3, 
#                           number = 10000) 
#   
#     # priniting minimum exec. time 
#     print('Binary search time: {}'.format(min(times)))         
#   
#   
# # compute linear search time 
# def linear_time(): 
#     SETUP_CODE = ''' 
# from __main__ import linear_search 
# from random import randint'''
#       
#     TEST_CODE = ''' 
# mylist = [x for x in range(10000)] 
# find = randint(0, len(mylist)) 
# linear_search(mylist, find) 
#     '''
#     # timeit.repeat statement 
#     times = timeit.repeat(setup = SETUP_CODE, 
#                           stmt = TEST_CODE, 
#                           repeat = 3, 
#                           number = 10000) 
#   
#     # priniting minimum exec. time 
#     print('Linear search time: {}'.format(min(times)))   
#   
# if __name__ == "__main__": 
#     linear_time() 
#     binary_time() 
# 
# =============================================================================
# =============================================================================
# import numpy as np
# arr = np.array( [[ 1, 2, 3], 
#                  [ 4.09, 2, 5]] ) 
# # Printing type of arr object 
# print("Array is of type: ", type(arr)) 
#   
# # Printing array dimensions (axes) 
# print("No. of dimensions: ", arr.ndim) 
#   
# # Printing shape of array 
# print("Shape of array: ", arr.shape) 
#   
# # Printing size (total number of elements) of array 
# print("Size of array: ", arr.size) 
#   
# # Printing type of elements in array 
# print("Array stores elements of type: ", arr.dtype)
# print(arr)
# =============================================================================

# Python program to demonstrate 
# array creation techniques 
import numpy as np 
# =============================================================================
#   
# # Creating array from list with type float 
# a = np.array([[1, 2, 4], [5, 8, 7]])#, dtype = 'float') 
# print ("Array created using passed list:\n", a) 
#   
# # Creating array from tuple 
# b = np.array((1 , 3, 2)) 
# print ("\nArray created using passed tuple:\n", b) 
#   
# # Creating a 3X4 array with all zeros 
# c = np.zeros((3, 4)) 
# print ("\nAn array initialized with all zeros:\n", c) 
#   
# # Create a constant value array of complex type 
# d = np.full((3, 3), 6, dtype = 'complex') 
# print ("\nAn array initialized with all 6s." 
#             "Array type is complex:\n", d) 
#   
# # Create an array with random values 
# e = np.random.random((2, 2)) 
# print ("\nA random array:\n", e) 
#   
# # Create a sequence of integers  
# # from 0 to 30 with steps of 5 
# f = np.arange(0, 30, 5) 
# print ("\nA sequential array with steps of 5:\n", f) 
#   
# # Create a sequence of 10 values in range 0 to 5 
# g = np.linspace(0, 5, 10) 
# print ("\nA sequential array with 10 values between"
#                                         "0 and 5:\n", g) 
#   
# # Reshaping 3X4 array to 2X2X3 array 
# arr = np.array([[1, 2, 3, 4], 
#                 [5, 2, 4, 2], 
#                 [1, 2, 0, 1]]) 
#   
# newarr = arr.reshape(2, 2, 3) 
#   
# print ("\nOriginal array:\n", arr) 
# print ("Reshaped array:\n", newarr) 
#   
# # Flatten array 
# arr = np.array([[1, 2, 3], [4, 5, 6]]) 
# flarr = arr.flatten() 
#   
# print ("\nOriginal array:\n", arr) 
# print ("Fattened array:\n", flarr) 
# =============================================================================

# =============================================================================
# # An exemplar array 
# arr = np.array([[-1, 2, 0, 4], 
#                 [4, -0.5, 6, 0], 
#                 [2.6, 0, 7, 8], 
#                 [3, -7, 4, 2.0]]) 
#   
# # Slicing array 
# temp = arr[:2, ::2] 
# print ("Array with first 2 rows and alternate"
#                     "columns(0 and 2):\n", temp) 
#   
# # Integer array indexing example 
# temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
# print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
#                                     "(3, 0):\n", temp) 
#   
# # boolean array indexing example 
# cond = arr > 0 # cond is a boolean array 
# print("cond", cond)
# temp = arr[cond] 
# print ("\nElements greater than 0:\n", temp) 
# =============================================================================
# =============================================================================
# a = np.array([1, 2, 5, 3]) 
#  
# # add 1 to every element 
# print ("Adding 1 to every element:", a+1) 
#   
# # subtract 3 from each element 
# print ("Subtracting 3 from each element:", a-3) 
#   
# # multiply each element by 10 
# print ("Multiplying each element by 10:", a*10) 
#   
# # square each element 
# print ("Squaring each element:", a**2) 
#   
# # modify existing array 
# a *= 2
# print ("Doubled each element of original array:", a) 
#   
# # transpose of array 
# a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
#   
# print ("\nOriginal array:\n", a) 
# print ("Transpose of array:\n", a.T) 
# =============================================================================
# =============================================================================
# arr = np.array([[1, 5, 6], 
#                 [4, 7, 2], 
#                 [3, 1, 9]]) 
#   
# # maximum element of array 
# print ("Largest element is:", arr.max()) 
# print ("Row-wise maximum elements:", 
#                     arr.max(axis = 1)) 
#   
# # minimum element of array 
# print ("Column-wise minimum elements:", 
#                         arr.min(axis = 0)) 
#   
# # sum of array elements 
# print ("Sum of all array elements:", 
#                             arr.sum()) 
#   
# # cumulative sum along each row 
# print ("Cumulative sum along each row:\n", 
#                         arr.cumsum(axis = 1))
# =============================================================================
# =============================================================================
# a = np.array([[1, 2], 
#             [3, 4]]) 
# b = np.array([[4, 3], 
#             [2, 1]]) 
#   
# # add arrays 
# print ("Array sum:\n", a + b) 
#   
# # multiply arrays (elementwise multiplication) 
# print ("Array multiplication:\n", a*b) 
#   
# # matrix multiplication 
# print ("Matrix multiplication:\n", a.dot(b))
# 
# =============================================================================

# =============================================================================
# # create an array of sine values 
# a = np.array([0, np.pi/2, np.pi]) 
# print ("Sine values of array elements:", np.sin(a)) 
#   
# # exponential values 
# a = np.array([0, 1, 2, 3]) 
# print ("Exponent of array elements:", np.exp(a)) 
#   
# # square root of array values 
# print ("Square root of array elements:", np.sqrt(a)) 
# =============================================================================





































