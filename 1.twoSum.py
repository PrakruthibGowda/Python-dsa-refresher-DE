""" 
Given an array of integers 'nums' and an integer 'target', return the indices of the two numbers such that they add up to target. 
Input : nums = [2, 7, 11, 15], target = 9 
Output : (0,1) or [0,1] 
""" 

""" 
Bruteforce method : 
T = O(n*n) becuase of nested loop 
S = O(1) doesn't construct new data structure
""" 

def twoSum(nums,target): 
  n=len(nums) 
  for i in range(n):
    
    for j in range(i+1,n):
      
      if nums[i] + nums[j] == target:
        return [i,j] 
        
""" 
Optimised solution : 
T = O(n) single looping through the list 
S = O(n) dictionary construction 
""" 

def twoSumOptimised(nums,target):
  checked = {} 
  
  for i,num in enumerate(nums):
    needed = target - num
    
    if needed in checked:
      return [i,checked[needed]]
    checked[num] = i

