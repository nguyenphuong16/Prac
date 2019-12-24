class Thing:

 def __init__(self, a, b):
  self.a = a
  self.b = b



 def change(self, b):

  self.a += b



it = Thing(5, 6)

it.change(2)

print(it.a, it.b)