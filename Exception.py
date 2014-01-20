try:
  c=8/6
except(ZeroDivisionError):
  print('Divide by Zero Error')
except(TypeError):
  print('you entered a string')
else:
  print("No error or other error")
finally:
  print("Program executes")
