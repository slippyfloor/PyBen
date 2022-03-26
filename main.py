import random

print("Ben?")
foo = ['Yes', 'No', 'Eaugh', 'Hohoho!']
while True:
  benin = input()
  if benin == "":
    pass
  else:
    print(random.choice(foo))
