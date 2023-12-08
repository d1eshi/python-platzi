import random

options = ('rock', 'papper', 'scissors')

user_option_choosed = input('rock (press 1)? papper (press 2)? scissors (press 3)?')
pc_option = random.choice(options)
# rules = [[1, 1] = false]

 
def showText():
  return f'You choosed {user_option_choosed} and the pc choosed {pc_option}'

def game():
  if pc_option == user_option_choosed:
    print('TIED', showText())
  elif (user_option_choosed == 1 and pc_option == 3) or (user_option_choosed == 2 and pc_option == 1) or (user_option_choosed == 3 and pc_option == 2):
    print('YOU WIN!!', showText())
  else: print('LOSER', showText())

game()