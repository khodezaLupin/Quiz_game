print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
print(playing)
if playing.lower() !="yes":
      quit()
print("Okay! Let's :) ")
answer = input("What does CPU stand for?  ")
if answer.lower() =="central processing unit":
      print('Correct!')
else:
      print("Incorrect oops!")
          
answer = input("What does GPU stand for?  ")
if answer.lower() =="graphics processing unit":
      print('Correct!')
else:
      print("Incorrect oops!") 
answer = input("What does RAM stand for?  ")
if answer=="random access memory":
      print('Correct!')
else:
      print("Incorrect oops!") 
answer = input("What does PSU stand for?  ")
if answer=="power supply":
      print('Correct!')
else:
      print("Incorrect oops!")                                  