#matrix as
a=[[1,2,3],[2,4,6],[3,6,9]]
for i in range(3):
  for j in range(3):
    a[i][j]=eval(input("enter value"))
  print(a)
for i in range(3):
  for j in range(3):
    print(a[i][j],end='')
  print()
