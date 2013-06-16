# string_times 
# http://codingbat.com/prob/p193507
# Given a string and a non-negative int n, return a larger string that is n copies of the original string. 
def string_times(str, n):
  return str*n


# front_times
# http://codingbat.com/prob/p165097 
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front; 
def front_times(str, n):
  if str <= 3:
    return str * n
  return str[:3]*n

# string_bits
# http://codingbat.com/prob/p113152
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo". 
def string_bits(str):
  if len(str) == 0:
    new_word = ""
  else:
    new_word = str[:1]
  for c in str:
    if c%2 == 0:
      new_word = new_word + str[c]
  return new_word


# string_splosion
# http://codingbat.com/prob/p118366
# Given a non-empty string like "Code" return a string like "CCoCodCode". 
def string_splosion(str):
  reps = len(str) + 1
  text = ""
  for i in range(reps):
    text = text + str[:i]
  
  return text


# last2
# http://codingbat.com/prob/p145834
# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). 
def last2(str):
  # catch any strings too short to meet criteria
  if len(str)<=3:
    return 0
  
  # get the last two characters and set default response
  response = 0
  last2 = str[-2:]
  
  if last2 in str[:-2]:
    response = str.count(str[-2:])-1

  return response
  

# array_count9
# http://codingbat.com/prob/p166170
# Given an array of ints, return the number of 9's in the array. 
def array_count9(nums):
  # a "lazy" dev can just:
  # return nums.count(9)
  count = 0
  for i in nums:
    if i == 9:
      count = count + 1
  return count


# array_front9
# http://codingbat.com/prob/p110166
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4. 
def array_front9(nums):
  maxreps = 4
  counts = False
  if len(nums) < 1:
    return False
    
  for num in range(len(nums)):
    if (num != maxreps) and (nums[num] == 9):
      counts = True
  return counts


# array123
# http://codingbat.com/prob/p193604
# Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere. 
def array123(nums):
  for num in range(len(nums)-2):
    if (nums[num] == 1) and (nums[num+1] == 2) and (nums[num+2] == 3):
      return True
  return False


# string_match
# http://codingbat.com/prob/p182414
# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings. 
def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  if len(a) < 1:
    return count
  for i_char in range(shorter-1):
    count = count + b.count(a[i_char:i_char+2])
  return count
      
