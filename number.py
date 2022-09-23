import random
def game():
  number = random.randint(1,50)
  if number <= 25 :
     print("Your number is equal or smaller than 25")
  else:
      print("your number is higher than 25 and lower or equal to 50 ")
      print(number) 

  admin_tricks = input("enter enything to continue \n")
  if admin_tricks == "im admin":
    print(str(number)  + " for admin use only ;)") 
  else: print("")
  answear = input("Guess the random number!! \n")
  
  if answear == str(number):
    print("Well done!!")
  elif answear == "im admin":
    print(number)
  else: 
    print("the real number was " + str(number))

game()