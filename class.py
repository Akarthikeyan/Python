class person():
  name=" "
  mark=1
  def display(self):
    print("person name is {0} \n person mark is {1}".format(self.name,self.mark))
obj=person()
obj.name="kar"
obj.mark=100
obj.display()
