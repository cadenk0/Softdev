def makes10(a, b):
  if a == 10 or b == 10 or a + b == 10:
	return True
  else:
	return False

def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200 - n) <= 10

def pos_neg(a, b, negative):
  if negative:
	return a < 0 and b < 0
  else:
	return a/b < 0

def not_string(str):
  if str[:3] == "not":
	return str
  else:
	return "not " + str

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  if len(str) <= 1:
	return str
  front = str[0]
  back = str[len(str)-1]
  if len(str) == 2:
	return back + front
  else:
	return back + str[1:len(str)-1] + front

def front3(str):
  rep = ""
  if len(str) < 3:
	rep = str
  else:
	rep = str[:3]
  return rep + rep + rep

