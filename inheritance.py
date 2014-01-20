class candidate:
  name=" "
  mark=0
  def display(self)
class studies(candidate):
  book="The Sachin"
  rank=1
  def play(self):
    print("read the book",self.book)
    print("rank",self.rank)
  s=studies()
  s.display()
  s.play()
