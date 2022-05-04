s = int(input())
one = s // 100
two = s % 100
if one > 12:
  if two > 12 or two == 0:
    print("NA")
  else:
    print("YYMM")
elif two > 12:
  if one > 12 or one == 0:
    print("NA")
  else:
    print("MMYY")
else:
  if one == 0 and two == 0:
    print("NA")
  elif one == 0:
    print("YYMM")
  elif two == 0:
    print("MMYY")
  elif one < 13 and two < 13:
    print("AMBIGUOUS")
  else:
    print("NA")

