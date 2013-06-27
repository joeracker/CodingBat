# =============================================
# Logic-1.py

# =======================
# http://codingbat.com/prob/p158497
def in1to10(n, outside_mode):
  if outside_mode and (n <= 1 or n >= 10):
    return True
  elif outside_mode == False and n in range(1,11):
    return True
  else:
    return False

# =======================
# http://codingbat.com/prob/p116620
def sorta_sum(a, b):
  sum = a+b
  if sum >= 10 and sum <= 19:
    return 20
  else:
    return sum
# =======================
# http://codingbat.com/prob/p119867
def alarm_clock(day, vacation):
  if (day == 0 or day == 6) and vacation:
    return "off"
  elif (day == 0 or day == 6) or vacation:
    return "10:00"
  else:
    return "7:00"
# =======================
# http://codingbat.com/prob/p137202
def caught_speeding(speed, is_birthday):
  if is_birthday: speed = speed - 5
  if speed <= 60:
    return 0
  elif speed >60 and speed <=80:
    return 1
  else:
    return 2

# =======================
# http://codingbat.com/prob/p135815
def squirrel_play(temp, is_summer):
  if is_summer and (temp >= 60 and temp <=100):
    return True
  elif temp >= 60 and temp <= 90:
    return True
  else:
    return False

# =======================
# http://codingbat.com/prob/p195669
def cigar_party(cigars, is_weekend):
  return (is_weekend and cigars >= 40) or (cigars >=40 and cigars <= 60)

# =======================
# http://codingbat.com/prob/p129125
def date_fashion(you, date):
  if you < 3 or date < 3:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1

# =======================
# http://codingbat.com/prob/p165321
def near_ten(num):
  remainder = num % 10
  return remainder <= 2 or remainder >= 8
# =======================
# http://codingbat.com/prob/p100958
def love6(a, b):
  if a+b == 6 or abs(a-b) == 6:
    return True
  elif a == 6 or b == 6:
    return True
  else:
    return False
