"""

You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s. 
Write a solution to sort this array/list in a 'single scan'.

Single Scan' refers to iterating over the array/list just once or to put it in other words, you will be visiting each 
element in the array/list just once
"""



n=int(input()) 
for i in range(0,n): 
    m=int(input()) 
    a=list(input().split()) 
    a.sort() 
    b=' '.join([str(ele) for ele in a]) 
print(b)