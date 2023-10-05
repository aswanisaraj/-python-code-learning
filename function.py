#function_practice 01
 def f():
  return 500 * 90
 result = f()
 print(result)





#function_practice 02
 def f(x, y, z):
     return x + y + z
 result = f(1, 2, 3)
 print(result)





#function_practice 03
 def f(x=10):
  if x == 10:
      print('x is ten')
  else:
      print('x is not ten ')
 default = f()
 pass_in = f(2)
 print(default)
 print(pass_in)

 age = input("How old are you?")
 age = int(age)
 if age < 21:
     print("You are young!")
 else:
     print("Wow you are old!")



#function_practice 04

def divide():
    a_str = input('Type a number: ')
    b_str = input('Type another number: ')
    try:
        a = float(a_str)
        b = float(b_str)
        result = a / b
        print(result)
    except ZeroDivisionError:
        print('Error: the second number cannot be zero. Please try again.')

