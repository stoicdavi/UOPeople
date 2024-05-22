def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False
print(any_lowercase1('Head'))