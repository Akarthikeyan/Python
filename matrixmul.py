a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[2,4,6],[3,6,9],[2,4,8]]
for i in range(3):
  for j in range(3):
    for k in range(3):
      c=a[i][j]*b[i][j]
    print(" ",c,end='')
  print()
