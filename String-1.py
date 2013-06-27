=============================================
String-1.py
# =======================
# http://codingbat.com/prob/p129981
def make_out_word(out, word):
  return out[:2] + word + out[2:]

# =======================
# http://codingbat.com/prob/p115413
def hello_name(name):
  return 'Hello %s!' % name

# =======================
# http://codingbat.com/prob/p127703
def non_start(a, b):
  return '%s%s' %(a[1:],b[1:])

# =======================
# http://codingbat.com/prob/p132290
def make_tags(tag, word):
  return '<%s>%s</%s>' %(tag,word,tag)

# =======================
# http://codingbat.com/prob/p182144
def make_abba(a, b):
  return '%s%s%s%s' %(a,b,b,a)

# =======================
# http://codingbat.com/prob/p184816
def first_two(str):
  if str <= 2: return str
  return str[:2]

# =======================
# http://codingbat.com/prob/p148853
def extra_end(str):
  if str < 2: return 'poo'
  return str[-2:]*3

# =======================
# http://codingbat.com/prob/p107010
def first_half(str):
  return str[:len(str)/2]

# =======================
# http://codingbat.com/prob/p194053
def combo_string(a, b):
  maximum = max([a,b], key=len)
  minimum = min([a,b], key=len)
  #return ""
  return minimum + maximum + minimum
  #return min[a,b] + max[a,b] + min[a,b]

# =======================
# http://codingbat.com/prob/p138533
def without_end(str):
  return str[1:-1]

# =======================
# http://codingbat.com/prob/p160545
def left2(str):
  return '%s%s' %(str[2:],str[:2])
