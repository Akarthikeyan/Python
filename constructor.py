class person:
  name=" "
  mark=1
  def __init__(self,a,b):
    self.name=a
    self.mark=b
    print("constructor invoked")
  def display(self):
    print("person anme is {0} \n person mark is {1}".format(self.name,self.mark))
per=person('kar',90)
