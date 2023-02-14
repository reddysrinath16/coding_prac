#K'th smallest/largest element in an array

""" Explainantion - Given an array and a number K where K is smaller than size of array, we need to find the 
K'th smallest element and K'th largest element in the given array. It is given that all array 
elements are not distinct."""

#If element is not present, then return -1.
"""
1) Kth largest and smallest element in an array is the K'th element of the array when sorted in increasing order.
 For example consider the array {2, 1, 5, 6, 3, 3, 8} and K=4, the sorted array will be {1, 2, 3, 3, 5, 6, 8}.
 But we will check the array {1, 2, 3, 5, 6, 8} as 3 is repeated twice and the 4th largest element will be 3 and 
 4th smallest will be 5.

2) All the elements of the array are not distinct."""

"""
Detailed Explaination
The first line of the input contains an integer T denoting the number of test cases.

The first line of each test case contains two space-separated integers N and K, as described in the problem statement.

The second line of each test case contains N space-separated integers, representing the elements of the array.

"""
from os import *
from sys import *
from collections import *
from math import *

def kthSmallestLargest(arr,k):
    arr = list(set(arr))    
    if len(arr)<k:        
        return -1,-1    
    else:        
        return arr[k-1],arr[len(arr)-k]

t = int(input())

while t > 0:        
    n,k = map(int,input().split())    
    arr = [int(i) for i in input().split()]    
    small,large = kthSmallestLargest(arr,k)    
    print(large,small)        
    t -= 1 
