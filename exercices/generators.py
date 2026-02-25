class MyIterator:
   def __init__(self, max):
       self.max = max
       self.current = 1
   def __iter__(self):
       return self
   def __next__(self):
       if self.current <= self.max:
           number = self.current
           self.current += 1
           return number
       else:
           raise StopIteration
print("Iterator:")
for num in MyIterator(5):
   print(num)
def even_numbers(n):
   for i in range(n):
       if i % 2 == 0:
           yield i
print("\nGenerator:")
for num in even_numbers(10):
   print(num)
print("\nGenerator Expression:")
squares = (x*x for x in range(5))
for s in squares:
   print(s)
