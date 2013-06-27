=============================================
List-1.py
# =======================
# http://codingbat.com/prob/p113659
def make_pi():
  return [3,1,4]

# =======================
# http://codingbat.com/prob/p192589
def sum2(nums):
  if len(nums) == 0: return 0
  if len(nums) == 1: return nums[0]
  return nums[0] + nums[1]

# =======================
# http://codingbat.com/prob/p148661
def rotate_left3(nums):
  first = nums[0]
  nums.pop(0)
  nums.append(first)
  return nums
# =======================
# http://codingbat.com/prob/p181624
def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6

# =======================
# http://codingbat.com/prob/p135290
def max_end3(nums):
  big = max([nums[0],nums[-1]])
  for i in range(len(nums)):
    nums[i] = big
  return nums

# =======================
# http://codingbat.com/prob/p147755
def common_end(a, b):
  return (a[0] == b[0] or a[-1] == b[-1])
# =======================
# http://codingbat.com/prob/p192962
def reverse3(nums):
  reversed = []
  for i in nums:
    reversed.insert(0,i)
  return reversed
# =======================
# http://codingbat.com/prob/p171011
def middle_way(a, b):
  return [a[1],b[1]]
  

# =======================
# http://codingbat.com/prob/p179078
def same_first_last(nums):
  return len(nums) >=1 and nums[0] == nums[-1]

# =======================
# http://codingbat.com/prob/p124806
def make_ends(nums):
  return [nums[0],nums[-1]]

# =======================
# http://codingbat.com/prob/p177892
def has23(nums):
  return 2 in nums or 3 in nums

# =======================
# http://codingbat.com/prob/p191645
def sum3(nums):
  return sum(nums)
