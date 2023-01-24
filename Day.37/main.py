class stack():

  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def is_empty(self):
    return self.items == []

  def pop(self):
    return self.items.pop()

  def peek(self):
    if not self.is_empty():
      return self.items[-1]

  def get_items(self):
    return self.items


get_stack = stack()
get_stack.push("Apple")
print(get_stack.get_items())
get_stack.pop()
print(get_stack.is_empty())
print("OK")
