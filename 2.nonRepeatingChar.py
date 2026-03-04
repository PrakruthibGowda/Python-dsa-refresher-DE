"""
Given a string s, find the first non-repeating character in the string and return its index. If no such character exists, return -1.
Input : s = "leetcode"
Output : 0
Explanation: 'l' is the first character that appears only once.
"""

"""
Brute force 
Time Complexity: O(n²)
Outer loop: n
Inner loop: n

Space Complexity: O(1)
No extra data structures used.
"""

def nonRepChar(s):
  n = len(s)
  for i in range(n):
    count=0
    
    for j in range(n):
      if s[i]==s[j]:
        count+=1
        
    if count==1:
      return i
  return -1

"""
Optimal solution 
T = O(n+n+1) = O(n)
1 pass → build frequency dictionary
1 pass → find first unique character

Space Complexity: O(n)
Dictionary stores frequency of characters
"""

def nonRepeatingCharOpt(s):
  freq={}
  for ch in s:
    freq[ch] = freq.get(ch,0) +1

  for i,ch in enumerate(s):
    if freq[ch] ==1:
      return i

  return -1




