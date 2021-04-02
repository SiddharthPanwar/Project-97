import random
n = random.randint(1, 9)
guess = int(input("Enter an integer from 1 to 9: "))
while n != "guess":
  print
  if guess == n:

    print ("Congratulations You Won")

  else:

    print ("YOU LOSE!!!, The Number is", n)

    break

  print