=============================================
Warmup-2.py
# =======================
# http://codingbat.com/prob/p145834
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
# =======================
# http://codingbat.com/prob/p118366
def string_splosion(str):
  reps = len(str) + 1
  text = ""
  for i in range(reps):
    text = text + str[:i]
  
  return text

# =======================
# http://codingbat.com/prob/p113152
def string_bits(str):
  if len(str) == 0:
    new_word = ""
  else:
    new_word = str[:1]
  for c in str:
    if c%2 == 0:
      new_word = new_word + str[c]
  return new_word

# =======================
# http://codingbat.com/prob/p110166
def array_front9(nums):
  maxreps = 4
  counts = False
  if len(nums) < 1:
    return False
    
  for num in range(len(nums)):
    if (num != maxreps) and (nums[num] == 9):
      counts = True
  return counts
# =======================
# http://codingbat.com/prob/p182414
def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  if len(a) < 1:
    return count
  for i_char in range(shorter-1):
    count = count + b.count(a[i_char:i_char+2])
  return count
      
# =======================
# http://codingbat.com/prob/p193604
def array123(nums):
  for num in range(len(nums)-2):
    if (nums[num] == 1) and (nums[num+1] == 2) and (nums[num+2] == 3):
      return True
  return False
# =======================
# http://codingbat.com/prob/p165097
def front_times(str, n):
  if str <= 3:
    return str * n
  return str[:3]*n

# =======================
# http://codingbat.com/prob/p166170
def array_count9(nums):
  # a "lazy" dev can just:
  #return nums.count(9)
  
  count = 0
  for i in nums:
    if i == 9:
      count = count + 1
  return count
# =======================
# http://codingbat.com/prob/p193507
def string_times(str, n):
  return str*n
