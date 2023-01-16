def divide_dec(func):
  def wrapper(a,b):
    if b>a:
      a,b =b,a
    return func(a,b)
  return wrapper

@divide_dec
def divison(a,b):
  result = a/b
  print(result)

divison(2,10)
