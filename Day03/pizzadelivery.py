print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#how much they need to pay based on their size choice.
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += "M"
elif size == "L":
  bill +=15
else:
  print("You typed wrong input.")
#based on pepperoni.
if pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

#based on extra cheese.
if extra_cheese == "Y":
  bill += 2

print(f"Your final bill is: ${bill}.")