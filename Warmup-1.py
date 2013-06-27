=============================================
Warmup-1.py
# =======================
# http://codingbat.com/prob/p147920
def front3(str):
  if len(str) <= 3:
    return str*3
  
  front = str[:3]
  return front *3
# =======================
# http://codingbat.com/prob/p153599
def front_back(str):
  foo = list(str)
  if len(foo) <= 0: return ""
  length = len(foo) - 1
  first = foo[0]
  last = foo[length]
  foo[0] = last
  foo[length] = first
  return ''.join(foo)
# =======================
# http://codingbat.com/prob/p124984
def makes10(a, b):
  sum = a+b
  return(sum == 10 or (a == 10 or b == 10))

# =======================
# http://codingbat.com/prob/p120546
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  else:
    return False
  
  

# =======================
# http://codingbat.com/prob/p197466
def diff21(n):
  if n > 21:
    return 2*(n-21)
  return 21-n

# =======================
# http://codingbat.com/prob/p189441
def not_string(str):
  if str.startswith("not"):
    return str
  return "not " + str
# =======================
# http://codingbat.com/prob/p166884
def parrot_trouble(talking, hour):
  return (hour < 7 or hour > 20) and talking

# =======================
# http://codingbat.com/prob/p141905
def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  return a + b

# =======================
# http://codingbat.com/prob/p149524
def missing_char(str, n):
  foo = list(str)
  del foo[n]
  return ''.join(foo)
# =======================
# http://codingbat.com/prob/p173401
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  return False


# =======================
# http://codingbat.com/prob/p162058
def pos_neg(a, b, negative):
  if a < 0 and b < 0 and negative == True:
    return True
  if (a < 0 and b > 0) and not negative:
    return True
  if (a > 0 and b < 0) and not negative:
    return True
  return False

# =======================
# http://codingbat.com/prob/p124676
def near_hundred(n):
  if (abs(100 - n) < 11) or (abs(200-n)<11):
    return True
  return False
