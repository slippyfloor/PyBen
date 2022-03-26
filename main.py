import random

print("Ben?")
BenMsg = ['Yes', 'No', 'Eaugh', 'Hohoho!']
while True:
  benin = input()
  if benin == "":
    pass
  else:
    print(random.choice(BenMsg))
