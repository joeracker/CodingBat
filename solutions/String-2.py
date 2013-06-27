# =============================================
# String-2.py

# =======================
# http://codingbat.com/prob/p164876
def cat_dog(str):
  #Quickest, most pain free solution
  #return str.count('cat') == str.count('dog')
  
  #Longer solution if you don't have google
  cat_count = 0
  dog_count = 0
  for i in range(len(str)):
    if 'cat' in str[i:i+3]: cat_count = cat_count+1
    if 'dog' in str[i:i+3]: dog_count = dog_count+1
  return dog_count == cat_count
# =======================
# http://codingbat.com/prob/p149391
def xyz_there(str):
  newstr = str
  for '.xyz' in str:
    newstr = newstr.replace(".xyz", "")
  
  return ('xyz' in str)
# =======================
# http://codingbat.com/prob/p170842
def double_char(str):
  new_str = ""
  for i in str:
    new_str = new_str + i + i
  return new_str

# =======================
# http://codingbat.com/prob/p167246
def count_hi(str):
  #return str.count('hi')
  count = 0
  for i in range(len(str)):
    if 'hi' in str[i:i+2]:
      count = count + 1
  return count
# =======================
# http://codingbat.com/prob/p174314
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  #if a.endswith(b):
  #  return True
  #elif b.endswith(a):
  #  return True
  #else:
  #  return False
    
  return (a.endswith(b) or b.endswith(a))
# =======================
# http://codingbat.com/prob/p186048
def count_code(str):
  #The fastest solution would probably involve a regex
  # research regex for python
  
  #The longer solution:
  count = 0
  for i in range(len(str)-3):
    if 'co' == str[i:i+2] and 'e' == str[i+3]:
      count = count + 1
  return count