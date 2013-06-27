# =============================================
# Logic-2.py

# =======================
# http://codingbat.com/prob/p160533
def close_far(a, b, c):
  if abs(b - c) < 2: return False
  b_distance = abs(a - b)
  c_distance = abs(a - c)
  close = min(b_distance,c_distance)
  far = max(b_distance,c_distance)
  
  return (close <= 1 and far >= 2)
# =======================
# http://codingbat.com/prob/p118406
def make_bricks(small, big, goal):
  return small + (big*5) >= goal and goal % 5 <= small

# =======================
# http://codingbat.com/prob/p100347
def no_teen_sum(a, b, c):
  list = [fix_teen(a), fix_teen(b), fix_teen(c)]
  return sum(list)


def fix_teen(n):
  if n in [15,16]: 
    return n
  elif n >= 13 and n <= 19:
    return 0
  return n
# =======================
# http://codingbat.com/prob/p190859
def make_chocolate(small, big, goal):
  # ensure that adding up everything will enable us to meet goal
  if not (small + (big*5)) >= goal:
    return -1
  
  # How many of our bigs do we need?
  big_gap = 0
  bigs_needed = big - (goal/5)
  if bigs_needed < 0:
    big_gap = abs(bigs_needed * 5)
  
  # How many smalls needed?  
  small_need = big_gap + (goal % 5)
  if small_need <= small:
    return small_need
  
  return -1
  
  # ensure there are enough smalls
  #if (goal-(5*big)) <= small:
  #  return abs((goal-(5*big)))
  #else:
  #  return -1
# =======================
# http://codingbat.com/prob/p143951
def lone_sum(a, b, c):
  list = [a,b,c]
  sum = 0
  
  for i in list:
    #if it is unique, add it to sum
    if list.count(i) == 1:
      sum = sum + i
    #if it has a pair, ignore it 
    elif list.count(i) >= 2:
      pass
  return sum
# =======================
# http://codingbat.com/prob/p107863
def lucky_sum(a, b, c):
  list = [a, b, c]
  sum = 0
  for i in list:
    if i == 13:
      return sum
    else:
      sum = sum + i
  return sum

# =======================
# http://codingbat.com/prob/p179960
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(num):
  mod = num % 10
  if mod >= 5:
    return num + (10-mod)
  elif mod <= 4:
    return num - mod
  else:
    return num
